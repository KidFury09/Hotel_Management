ids = {"Keshav" : ["Password","Manger"], "Hayden" : ["password", "Front_Desk"]}
#Assume Keshav is the manager and Hayden is the front desk clerk

print("Please login")
print()
User = input("Enter employee name: ")
Pass = input("Enter password: ")
print()

while True:
    if User in ids:
        psw = ids[User]
        if Pass == psw[0]:
            break
            # Manager or clerk interface
        else:
            print("Password is incorrect. Please try again")
            print()
            User = input("Enter employee name: ")
            Pass = input("Enter password: ")
            print()
    else:
        print("Name is incorrect. Please try again")
        print()
        User = input("Enter employee name: ")
        Pass = input("Enter password: ")
        print()