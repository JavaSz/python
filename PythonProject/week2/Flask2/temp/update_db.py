# -*- coding: utf-8 -*-
# @Time    : 2018/4/11 14:29
# @Author  : Zhang
# @FileName: update_db.py
# @Software: PyCharm
# @Blog    ：https://codedraw.cn
import sqlite3

conn = sqlite3.connect('flask.db')
c = conn.cursor()
print("Opened database successfully")

# c.execute("UPDATE COMPANY set SALARY = 25000.00 where ID=1")
c.execute("DELETE from COMPANY where ID=2;")
conn.commit()
print("Total number of rows updated :", conn.total_changes)

cursor = conn.execute("SELECT id, name, address, salary  from COMPANY")
for row in cursor:
   print("ID = ", row[0])
   print("NAME = ", row[1])
   print("ADDRESS = ", row[2])
   print("SALARY = ", row[3], "\n")

print("Operation done successfully")
conn.close()