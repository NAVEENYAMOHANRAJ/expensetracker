import argparse
import os
import json

file="expense.json"

def load_expense():
    if os.path.exists(file):
        with open(file,"r") as f:
            return json.load(f)
    return[]

expense=load_expense()

def save_expense():
    with open(file,"w") as f:
        json.dump(expense,f)

def add(args):
    expense1={}
    expense1["name"]=args.name
    expense1["price"]=args.price
    expense.append(expense1)
    save_expense()
    
def view_expense():
    for i in expense:
        print("name",i["name"],"price",i["price"])

def total():
    t=0
    for i in expense:
        t+=i["price"]
    print(t)

def delete_item(args):
    for i in expense:
        if i["name"]==args.name:
            expense.remove(i)
            save_expense()
            break
    else:
        print("item not found")
    print(expense)

   
def update_item(args):
    for i in expense:
        if i["name"]==args.name:
            i["price"]=args.price
            save_expense()
            break
    else :
        print("item not found")
    print(expense)
    
def search_expenses(args):
    for i in expense:
        if i["name"]==args.name:
            print(i["price"])
            break
    else :
        print("item not found")
    print(expense)

def add_category(args):
    for i in expense:
        if i["name"]==args.pname:
            i["categories"]=args.cname
            save_expense()
            break
    else:
        print("item not found")
    print(expense)
    
a=argparse.ArgumentParser()

sub=a.add_subparsers(dest="command")

#add product and expense
add_product=sub.add_parser("add",help="add expenses")
add_product.add_argument("--name",required=True,help="product name")
add_product.add_argument("--price",type=int,required=True,help="product price")

#view_expense
view_expenses=sub.add_parser("view_expenses",help="view product and  expenses")

#total
total_expense=sub.add_parser("total_expense",help="total of expenses")
#delete
delete_item_=sub.add_parser("delete_item_",help="eneter product name you want to delete")
delete_item_.add_argument("--name",required=True)

#update price
update_price=sub.add_parser("update_price",help="enter name of product to update price")
update_price.add_argument("--name",required=True)
update_price.add_argument("--price",required=True,type=int)

#search_expenses
search_name=sub.add_parser("search_name",help="enter product name to find expense")
search_name.add_argument("--name",required=True)

#add_category(args)
add_new=sub.add_parser("add_new",help="add new category name ")
add_new.add_argument("--pname",required=True)
add_new.add_argument("--cname",required=True)

args=a.parse_args()
if args.command=="add":
    add(args)
elif args.command=="view_expenses":
    view_expense()
elif args.command=="total_expense":
    total()
elif args.command=="delete_item_":
    delete_item(args)
elif args.command=="update_price":
    update_item(args)
elif args.command=="search_name":
    search_expenses(args)
elif args.command=="add_new":
    add_category(args)
