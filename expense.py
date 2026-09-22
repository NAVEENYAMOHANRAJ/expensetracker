import argparse

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
        
#argparse
argparser=argparse.ArgumentParser()
sub=argparser.add_subparsers(dest="command")

#create row
create_row=sub.add_parser("insert_row")
create_row.add_argument("--id",type=int)
create_row.add_argument("--name",required=True)
create_row.add_argument("--category")
create_row.add_argument("--expense",type=int)
create_row.add_argument("--date_of_entry")

update_expenses=sub.add_parser("update_expenses")
update_expenses.add_argument("--expense",type=int,required=True)
update_expenses.add_argument("--name",required=True)

delete_expenses=sub.add_parser("delete_expenses")
delete_expenses.add_argument("--name",required=True)

view_expenses=sub.add_parser("view_expenses")

d=argparser.parse_args()


create_table()
if d.command=="insert_row":
    insert_row(d.id,d.name,d.expense,d.category,d.date_of_entry)
    view_expense()
elif d.command=="update_expenses":
    update_expense(d.expense,d.name)
    view_expense()
elif d.command=="delete_expenses":
    delete_expense(d.name)
    view_expense()
elif d.command=="view_expenses":
    view_expense()

