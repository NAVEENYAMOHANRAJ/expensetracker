import sqlite3

#to connect to mysql
def connect_sql():
    return sqlite3.connect("expense.db")

#to create a table
def create_table():
     conn=connect_sql()
     cursor=conn.cursor()
     cursor.execute(""" CREATE TABLE  IF NOT EXISTS expenses (id INT primary key   ,
name varchar(50) ,
expense int,
category varchar(50) ,
date_of_entry date)""")
     conn.commit()
     conn.close()

#to insert a row
def insert_row(id,name,expense,category,date_of_entry):
    a=connect_sql()
    b=a.cursor()
    b.execute(""" insert into expenses (id,name,expense,category,date_of_entry)
   values(?,?,?,?,?) """,(id,name,expense,category,date_of_entry))
    a.commit()
    a.close()

#to update name
def update_expense(expense,name):
    a=connect_sql()
    b=a.cursor()
    b.execute(""" update expenses set expense=? where name=?""",
    (expense,name))
    a.commit()
    a.close()

def delete_expense(name):
    a=connect_sql()
    b=a.cursor()
    b.execute("""delete from expenses where name=?""", (name,))
    a.commit()
    a.close()

def view_expense():
    a=connect_sql()
    b=a.cursor()
    b.execute(""" select * from expenses""")
    a=b.fetchall()
    for i in a:
        print(i)