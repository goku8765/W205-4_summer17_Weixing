import sys
import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

conn = psycopg2.connect(database="tcount", user="postgres", password="pass", host="localhost", port="5432")
cur = conn.cursor()

# all rows with counts between argument 1 and argument 2
cur.execute("SELECT word, count FROM tweetwordcount WHERE count BETWEEN %s AND %s ORDER by count DESC", (sys.argv[1], sys.argv[2]))
conn.commit()
records = cur.fetchall()
print(records)

# 20 rows with most counts
cur.execute("SELECT word, count FROM tweetwordcount ORDER by count DESC LIMIT 20")
conn.commit()
records = cur.fetchall()
print(records)

conn.close()
