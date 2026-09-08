expense=[{"name":"soap","price":120},{"name":"shampo","price":120}]
def add():
    expense1={}
    namee=input("enter name:")
    pricee=int(input("enter price"))
    expense1["name"]=namee
    expense1["price"]=pricee
    expense.append(expense1)
def view_expense():
    for i in expense:
        print("name",i["name"],"price",i["price"])
def total():
    t=0
    for i in expense:
        t+=i["price"]
    print(t)
def delete_item():
    a=input("enetr item to be deleted:")
    found=False
    for i in expense:
        if i["name"]==a:
            expense.remove(i)
            found=True
        else:
            print("item not found")
    if found:
        print("deleted succesfully ")
    else :
        print("item not found")
    print(expense)
def update_item():
    b=input("enter item name which you want to update:")
    c=int(input("enter price :"))
    found=False
    for i in expense:
        if i["name"]==b:
            found=True
    if found:
        i["price"]=c
    else :
        print("item not found")
    print(expense)
def search_expenses():
    d= input("name of product to search :")
    found=False
    for i in expense:
        if i["name"]==d:
            found=True
    if found:
        print(i["price"])
    else :
        print("item not found")
    print(expense)
def add_category():
    c=input("enetr name of what you want to add to dictionary :")
    d=input("value:")
    for i in expense:
        i[c]=d
    print(expense)
add()
print(expense)
view_expense()
total()
delete_item()
update_item()
search_expenses()
add_category()