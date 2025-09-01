import pymysql

# 
db = pymysql.connect(host="localhost",user="root",password="369852",database="mrsoft",charset="utf8")

# cursor()
cursor = db.cursor()

# 
data = [("Python（）", "Python", 99.00, "2024-1-10"),
        ("C（）", "C", 99.00, "2024-1-10"),
        ("PyQt", "Python", 99.00, "2024-1-10"),
        ("Python", "Python", 99.00, "2024-1-10"),
        ("Python", "Python", 99.00, "2024-1-10"),
        ]

try:
    # SQL，
    cursor.executemany("insert into books(name, category, price, publish_time) values (%s,%s,%s,%s)", data)
    # 
    db.commit()
except:
    # 
    db.rollback()

# 
db.close()