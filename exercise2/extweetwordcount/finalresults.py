import sys
import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

conn = psycopg2.connect(database="tcount", user="postgres", password="pass", host="localhost", port="5432")
cur = conn.cursor()

if len(sys.argv) == 1:
   cur.execute("SELECT word, count FROM tweetwordcount LIMIT 20")
   records = cur.fetchall()
   conn.commit()
   print (records)

else:
   for i in range(1, len(sys.argv)):
      cur.execute("SELECT word, count FROM tweetwordcount WHERE word = %s", (sys.argv[i],))
      conn.commit()
      records = cur.fetchone()
      print('Total number of occurrences of {} : {}'.format(records[0],records[1]))

conn.close()
