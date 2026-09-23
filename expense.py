import argparse

import database
        
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


database.create_table()
if d.command=="insert_row":
    database.insert_row(d.id,d.name,d.expense,d.category,d.date_of_entry)
    database.view_expense()
elif d.command=="update_expenses":
    database.update_expense(d.expense,d.name)
    database.view_expense()
elif d.command=="delete_expenses":
    database.delete_expense(d.name)
    database.view_expense()
elif d.command=="view_expenses":
    database.view_expense()

