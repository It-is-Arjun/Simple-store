import mysql.connector as sql 
import datetime

con = sql.connect(host='localhost',user='root',password='12345',database='shop')
cur = con.cursor()

def add():
    ch = 'y'
    while ch.lower()=='y':
        cur.execute("select * from item")
        result = cur.fetchall()
        if not result:
            ino = 1
            iname = input('enter utensil name: ')
            rate = int(input('enter rate of utensil: '))
            qty = int(input('enter number of stocks available: '))
            query = "insert into item values({},'{}',{},{})".format(ino, iname, rate, qty)
            cur.execute(query)
            con.commit()
            print('utensil added')
        else:
            ino = result[-1][0] + 1
            iname = input('enter utensil name: ')
            rate = int(input('enter rate of utensil: '))
            qty = int(input('enter number of stocks available: '))
            query = "insert into item values({},'{}',{},{})".format(ino, iname, rate, qty)
            cur.execute(query)
            con.commit()
            print('utensil added')
        ch = input('do you want to add more utensils (y/n): ')

    
def addsingle():
    cur.execute('select * from item')
    result = cur.fetchall()
    if not result:
        ino = 1
    else:
       ino = result[-1][0] + 1
       iname = input('enter name of utensil: ')
       rate = int(input('enter rate of the utensil: '))
       qty = int(input('enter number of stocks available: '))
       query = "insert into item values({},'{}',{},{})".format(ino, iname, rate, qty)
       cur.execute(query)
       con.commit()
       print('utensil added')

def display():
    query = 'select * from item'
    cur.execute(query)
    result = cur.fetchall()
    if not result:
        print('no items were found')
    else :
        print('ino \t name \t rate \t qty')
        for item in result:
            print("{}\t{}\t{}\t{}".format(item[0], item[1], item[2], item[3]))

def remove():
    display()
    ino = int(input('enter SL.No of utensil to remove :'))
    query = "delete from item where ino ={}".format(ino)
    cur.execute(query)
    con.commit()
    print('utensil removed successfully.')

def modify():
    display()
    ino = int(input('enter SI.No to modify: '))
    query = "select * from item where ino ={}".format(ino)
    cur.execute(query)
    result = cur.fetchone()
    if result is None:
        print('item not found')
    else:
        iname = input('enter new name for the utensil (press enter to keep current name ): ')
        rate = input('enter new rate (press enter to keep the current ): ')
        qty = input('enter new no of stocks(press enter to keep current): ')
        if iname == "":
            iname = result[1]
        if rate == "":
            rate = result[2]
        else:
            rate = int(rate)
        if qty == "":
            qty = result[3]
        else:
            qty = int(qty)
        query = "update item set iname= '{}', rate = {}, qty = {} where ino = {}". format(iname, rate, qty, ino)
        cur.execute(query)
        con.commit()
        print("utensil modified successfully.")
        display()

def search():
    search_term = input("enter the name of item to search: ")
    query = "select * from item where iname like '%{}%'".format(search_term)
    cur.execute(query)
    result = cur.fetchall()
    if not result:
        print('no utensils found in the matching term')
    else:
        print("INO\tNAME\tRATE\tQTY")
        for item in result:
            print("{}\t{}\t{}\t{}".format(item[0],item[1],item[2],item[3]))

def printbill(cname, dop):
    query = "select * from bill where cname ='{}' and dop ='{}'".format(cname,dop)
    cur.execute(query)
    result = cur.fetchall()
    if not result:
        print('No bill found for the given customer and date')
    else:
        print("*" * 100)
        print("\t\tCustomer name :'{}'\t\t date of purchase : '{}'".format(cname,dop))
        print("*" * 100)
        print("S.No\tITEM\tNAME\tRATE\tQTY\tAMOUNT")
        sno = 1
        total = 0
        for item in result:
            print(f"{sno}\t{item[2]}\t\t{item[3]}\t{item[4]}\t{item[5]}")
            sno +=1
            total += item[5]
        print("*" * 100)
        print(f"\t\t\t\t\t\t\t total amount:{total}")
        print("*" * 100)

def customer():
    display()
    ch ='y'
    cname = input('enter customer name: ')
    dop = datetime.date.today()
    while ch.lower() == 'y':
        ino = int(input('enter item no of required item: '))
        qty = int(input('enter required quantity: '))
        query = "select * from item where ino = {}".format(ino)
        cur.execute(query)
        item = cur.fetchone()
        if item is None :
            print('Item not found')
        else:
            tqty = item[3]
            if tqty < qty: 
                print('required quantity is not available')
            else:
                iname = item[1]
                rate = item[2]
                amt = qty * rate
                query = "insert into bill values('{}','{}','{}',{},{},{})".format(cname,dop,iname,rate,qty,amt)
                cur.execute(query)
                query = "update item set qty = qty-{} where ino={}".format(qty,ino)
                cur.execute(query)
                con.commit()
                print('Item added in Bill')
        ch = input('continue shopping(y/n): ')
    printbill(cname, dop)

def owner():
    while True:
        print(' _________________________________')
        print('|           OWNER MENU            |')
        print('|     1.ADD A SET OF UTENSILS     |')
        print('|     2. ADD A SINGLE UTENSIL     |')
        print('|     3. MODIFY UTENSILS          |')
        print('|     4. REMOVE A UTENSIL         |')
        print('|     5.DISPLAY ALL UTENSILS      |')
        print('|     6. SEARCH FOR UTENSIL       |')
        print('|     7. GO BACK TO MAIN MENU     |')
        print('|_________________________________|')
        ch = int(input('enter your choice(1-7): '))
        if ch == 1:
            add()
        elif ch == 2:
            addsingle()
        elif ch == 3:
            modify()
        elif ch == 4:
            remove()
        elif ch == 5:
            display()
        elif ch == 6:
            search()
        elif ch == 7:
            break
        else:
            print('invalid choice try again')


while True:
    print(' _______________________')
    print('|        MAIN MENU      |')
    print('|       1. OWNER        |')
    print('|       2. CUSTOMER     |')
    print('|       3. EXIT         |')
    print('|_______________________|')
    choice = input('enter choice(1-3):')
    if choice == '1':
        owner()
    elif choice == '2':
        customer()
    elif choice == '3':
        break
    else:
        print('invalid try again')

cur.close()
con.close()