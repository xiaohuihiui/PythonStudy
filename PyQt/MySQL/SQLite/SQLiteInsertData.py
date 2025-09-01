import sqlite3

#  SQLite 
#  mrsoft.db
# ，
conn = sqlite3.connect('mrsoft.db')

#  Cursor
cursor = conn.cursor()

#  SQL , 
#  user 
cursor.execute('insert into user (id, name) values ("1", "MRSOFT")')
cursor.execute('insert into user (id, name) values ("2", "Andy")')
cursor.execute('insert into user (id, name) values ("3", "")')

# 
cursor.close()

# 
conn.commit()

#  Connection
conn.close()