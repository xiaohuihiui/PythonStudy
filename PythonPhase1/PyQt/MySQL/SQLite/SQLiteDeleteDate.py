import sqlite3

# SQLite, mrsoft.db
conn = sqlite3.connect('mrsoft.db')

# Cursor
cursor = conn.cursor()

# ID1
cursor.execute('delete from user where id = ?',(1,))

# 
cursor.execute('select * from user')

# 
result = cursor.fetchall()
print(result)

# 
cursor.close()

# 
conn.commit()

# Connection:
conn.close()