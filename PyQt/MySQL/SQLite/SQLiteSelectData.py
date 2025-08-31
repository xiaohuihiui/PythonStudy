import sqlite3

# SQLite, mrsoft.db
conn = sqlite3.connect('mrsoft.db')

# Cursor
cursor = conn.cursor()

# 
# cursor.execute('select * from user')
cursor.execute('select * from user where id = ?', (2, ))
# 
# 
# result1 = cursor.fetchone()
# result1 = cursor.fetchmany(5)
result1 = cursor.fetchall()
print(result1)

# 
cursor.close()

# Connection
conn.close()