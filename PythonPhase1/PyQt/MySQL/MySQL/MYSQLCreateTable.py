import pymysql

# 
db = pymysql.connect(host="localhost",user="root",password="369852",database="mrsoft")

#  cursor()  cursor
cursor = db.cursor()

#  execute()  SQL, 
cursor.execute("DROP TABLE IF EXISTS books")

# 
sql = """
CREATE TABLE books (
    id int(8) NOT NULL AUTO_INCREMENT,
    name varchar(50) NOT NULL,
    category varchar(50) NOT NULL,
    price decimal(10,2) DEFAULT NULL,
    publish_time date DEFAULT NULL,
    PRIMARY KEY (id)
) ENGINE=MyISAM AUTO_INCREMENT=1 DEFAULT CHARSET=utf8;
"""

# SQL
cursor.execute(sql)

# 
db.close()