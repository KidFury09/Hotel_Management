import mysql.connector as mql

obj = mql.connect(host = "localhost", user = "root", passwd = "hayden", database = "emp")
cr = obj.cursor()

def display():
    cr.execute("select * from emp")
    x = cr.fetchall()

    print("{:^9}{:^30}{:^15}{:^10}".format("Id", "Name", "Department", "Salary"))

    for i in x:
        print("{:^9}{:^30}{:^15}{:^10}".format(i[0], i[1], i[2], i[3]))
    print()

def search():
    id = int(input("Enter the employee id: "))
    cr.execute(f"select * from emp where empid = {id}")
    x = cr.fetchone()

    print("{:^9}{:^30}{:^15}{:^10}".format("Id", "Name", "Department", "Salary"))
    print("{:^9}{:^30}{:^15}{:^10}".format(x[0], x[1], x[2], x[3]))
    print()

def add():
    print("Enter the new employee information")
    id = int(input("Id: "))
    name = input("Name: ")
    dept = input("Department: ")
    sal = int(input("Salary: "))

    cr.execute(f"insert into emp values ({id}, '{name}', '{dept}, {sal}')")
    cr.commit()
    print()

def update():
    print("Enter the employee id to be changed")
    id = int(input("Id: "))
    name = input("Name: ")
    dept = input("Department: ")
    sal = int(input("Salary: "))

    cr.execute(f"update emp set name = '{name}', dept = '{dept}', salary = {sal} where empid = {id}")
    cr.commit()
    print()

def delete():
    id = int(input("Enter the Id to be deleted: "))
    cr.execute(f"delete from emp where empid = {id}")
    cr.commit()
    print()

