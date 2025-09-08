import sqlite3

# SQLITE
# mrsoft.db, ，
conn = sqlite3.connect('mrsoft.db')

# Cursor
cursor = conn.cursor()

# SQL，user
cursor.execute('create table user (id int(10) primary key, name varchar(20))')

# 
cursor.close()

# Connection
conn.close()