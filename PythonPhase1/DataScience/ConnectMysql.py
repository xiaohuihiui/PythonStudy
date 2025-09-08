import pymysql

conn = pymysql.connect(host='localhost',port=3306,user='root',passwd='369852',db='sciencedata',charset='utf8')
cursor = conn.cursor(pymysql.cursors.DictCursor)
cursor.execute('select * from data')
result=cursor.fetchall()
print(result)

