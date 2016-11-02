# coding:utf-8

import mysql.connector

conn = mysql.connector.connect(host='192.168.3.51', user='web', password='Hello123', database='r')
cursor = conn.cursor()

cursor.execute('create table  if not EXISTS users(id int primary key, name varchar(32));')
cursor.execute('insert into users(id, name) VALUES (1, \'eagle\'), (2, \'michael\');')

cursor.execute('select * from users;')
values = cursor.fetchall()
print(values)
cursor.close()
conn.close()

from sqlalchemy import Column, String, Integer, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id =Column(Integer(), primary_key=True)
    name = Column(String(32))

engine = create_engine('mysql://web:Hello123@192.168.3.51/r')
DBSession = sessionmaker(bind=engine)

session = DBSession()
new_user = User(id=5, name='bob')
session.add(new_user)
session.commit()
session.close()


session = DBSession()
user = session.query(User).filter(User.id==5).one()
print(type(user))
print(user)
session.close()


