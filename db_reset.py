import pymysql
import time

conn = pymysql.connect(host="127.0.0.1", user="root", password="airmonitor", db="air", charset='utf8')
cursor = conn.cursor()
sql = '''
        TRUNCATE dust
      ''' 
cursor.execute(sql)
print('DB_TRUNCATE OK')
conn.commit()
conn.close()
