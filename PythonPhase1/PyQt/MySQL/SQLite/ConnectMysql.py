import pymysql

conn=pymysql.connect(host='localhost',user='root',passwd='369852',db='sciencedata',charset='utf8')
print(conn)
conn.commit()
conn.close()
