import pymysql

# , 1:IP; 2:; 3:; 4:
db = pymysql.connect(host="localhost",user="root",password="369852",database="mrsoft")

#  cursor()  cursor
cursor = db.cursor()

#  execute()  SQL 
cursor.execute("SELECT VERSION()")

#  fetchone() 
data = cursor.fetchone()

print ("Database version : %s" % data)

# 
db.close()