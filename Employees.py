import mysql.connector as mql
from time import sleep

obj = mql.connect(host = "localhost", user = "root", passwd = "hayden", database = "hotel")
cr = obj.cursor()

def display():
    print()
    cr.execute("select * from emp")
    x = cr.fetchall()

    print("{:^9}{:^30}{:^15}{:^10}".format("Id", "Name", "Department", "Salary"))

    for i in x:
        print("{:^9}{:^30}{:^15}{:^10}".format(i[0], i[1], i[2], i[3]))
    print()

def search():
    print()
    id = int(input("Enter the employee id: "))
    cr.execute(f"select * from emp where empid = {id}")
    x = cr.fetchone()

    if x == None:
        print("Id dosen't exist")

    else:
        print("{:^9}{:^30}{:^15}{:^10}".format("Id", "Name", "Department", "Salary"))
        print("{:^9}{:^30}{:^15}{:^10}".format(x[0], x[1], x[2], x[3]))
        print()

def add():
    print()
    while True:
        print("Enter the new employee information")
        id = int(input("Id: "))
        name = input("Name: ")
        dept = input("Department: ")
        sal = int(input("Salary: "))
        print()
        false = input("Enter Y to confirm details: ")

        if false.lower() == "y":
                break
        else:
            print("Renter data")
            print()

    cr.execute(f"insert into emp values ({id}, '{name}', '{dept}', {sal})")
    obj.commit()
    print()
    print(f"{id} has been cretaed")
    print()

def update():
    while True:    
        print()
        print("Enter the employee id to be changed")
        id = int(input("Id: "))
        name = input("Name: ")
        dept = input("Department: ")
        sal = int(input("Salary: "))
        print()
        false = input("Enter Y to confirm details: ")

        if false.lower() == "y":
                break
        else:
            print("Renter data")

    cr.execute(f"update emp set name = '{name}', dept = '{dept}', salary = {sal} where empid = {id}")
    obj.commit()
    print()
    print(f"{id} updated")
    print()

def delete():

    while True:
        print()
        id = int(input("Enter the Id to be deleted: "))

        false = input("Enter Y to confirm details: ")

        if false.lower() == "y":
            break
        else:
            print("Renter data")

    cr.execute(f"delete from emp where empid = {id}")
    obj.commit()
    print(f"{id} deleted from database")

def employee():
    while True:
        print()
        print("""Choose an option from below
        
        1) Employee Data
        2) Search Id
        3) Add Employee
        4) Update Id
        5) Delete Id
        6) Exit
        """)
        cho = input("Enter your option: ").lower()

        if cho == "1":
            display()
            sleep(2)

        elif cho == "2":
            search()
            sleep(2)

        elif cho == "3":
            add()
            sleep(2)

        elif cho == "4":
            update()
            sleep(2)

        elif cho == "5":
            delete()
            sleep(2)
            
        elif cho == "6":
            break
        else:
            print()
            print("Invalid entry")
