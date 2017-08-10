from __future__ import absolute_import, print_function, unicode_literals

from collections import Counter
from streamparse.bolt import Bolt

import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

conn = psycopg2.connect(database="tcount", user="postgres", password="pass", host="localhost", port="5432")
cur = conn.cursor()

class WordCounter(Bolt):

    def initialize(self, conf, ctx):
        self.counts = Counter()

    def process(self, tup):
        word = tup.values[0]
        self.counts[word] += 1
        cur.execute("SELECT EXISTS(SELECT word FROM tweetwordcount WHERE word=%s)", (word,))
        jud = cur.fetchone()[0]
        if not jud:
            cur.execute("INSERT INTO tweetwordcount (word,count) VALUES (%s, %s)", (word, self.counts[word]))
        else:
            cur.execute("UPDATE tweetwordcount SET count=%s WHERE word=%s", (self.counts[word], word))
        conn.commit()
        self.emit([word, self.counts[word]])
        
        # Log the count - just to see the topology running
        self.log('%s: %d' % (word, self.counts[word]))
