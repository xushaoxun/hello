# coding:utf-8
import sqlite3, os

# conn = sqlite3.connect('test.db')
# cursor = conn.cursor()
# cursor.execute('CREATE TABLE `user`(id int PRIMARY KEY , name varchar(20))')
# cursor.execute('INSERT INTO user(id, name) VALUES (1, \'Michael\')')
# cursor.execute('INSERT INTO user(id, name) VALUES (2, \'Eagle\')')
# cursor.close()
# conn.commit()
# conn.close()

db_file = (os.path.join(os.path.dirname(__file__), 'test.db'))
print(os.path.exists(db_file))
conn = sqlite3.connect('test.db')
cursor = conn.cursor()
cursor.execute('SELECT * from user')
values = cursor.fetchall()
print(values)
cursor.close()
conn.close()