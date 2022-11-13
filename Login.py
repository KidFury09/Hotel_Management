from hmng import manager

ids = {"Keshav" : ["Password","Manager"], "Hayden" : ["password", "Front_Desk"]}
#Assume Keshav is the manager and Hayden is the front desk clerk

print("Please login")
print()
User = input("Enter employee name: ")
Pass = input("Enter password: ")
print()
c = 0

while True:
    if User in ids:
        psw = ids[User]
        if Pass == psw[0] and psw[1] == "Manager":
            manager()
            c = 1
            if c == 1:
                break
        elif Pass == psw[0] and psw[1] == "Front_Desk":
            pass
            #check for which user; manager or front desk
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
