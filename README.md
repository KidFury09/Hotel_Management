# Hotel_Management
Grade 12 Computer Project

Code for creating the 75 rooms:
(Has to create the data base named "Hotel" and table named "Rooms" before hand)

Table should have:
RoomNo: int Primay Key
Guest: varchar(25)
NoGuest: int
PhoneNum: varchar(15)
Count: int

=========================================================================================================================================================================
import mysql.connector as mql

obj = mql.connect(host = "localhost", user = "root", passwd = "hayden", database = "hotel")

cr = obj.cursor()

for i in range(1,76):
    cr.execute(f"insert into rooms values ({i}, Null, Null, Null, 0)")
    obj.commit()

obj.close()
=========================================================================================================================================================================

Also table "Emp" in the same database

EmpId: int  Primay Key
Name: varchar(30)
Dept: varchar(12)
Salary: int
