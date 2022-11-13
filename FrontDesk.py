import mysql.connector as mql

obj = mql.connect(host = "localhost", user = "root", passwd = "hayden", database = "hotel")

cr = obj.cursor()

def room_count():
    print()
    c1 = 0
    c2 = 0
    c3 = 0
    c4 = 0

    cr.execute("select roomno ,Guest from rooms")
    x = cr.fetchall()

    for i in x:
        if i[0] in range(1,41) and i[1] == None: # 40 rooms
            c1+=1                
        elif i[0]  in range(41, 61) and i[1] == None: #20 rooms
            c2+=1
        elif i[0] in range(61,71) and i[1] == None: #10
            c3+=1
        else:   
            c4+=1 #5 rooms
    print(f'''Avaliable rooms
    Standard Rooms: {c1}
    Superior Rooms: {c2}
    Executive Rooms: {c3}
    Presidential Suite: {c4}
    ''')

def desk():

    while True:
        print()
        print("""Please Chose An Option
    1) Adding Guest
    2) Removing Guest
    3) Exit""")
        print()

        cho = input("Enter your choice here: ")
        print()
        if cho == "1":
            while True:
                guest = input("Customer name: " )
                pnum = input("Phone number: ")
                print()
                guest_n = int(input("Number of Guests: "))
                print()
                false = input("Enter Y to confirm details: ")

                if false.lower() == "Y":
                    break
                else:
                    print("Renter data")
                    print()
            print()
            
            room_count()
            while True:
                print()
                print("Enter the room type below: ")
                print()
                r1 = input("Standard Room(s): ")
                r2 = input("Superior Room(s): ")
                r3 = input("Executive Room(s): ")
                r4 = input("Presidential Suite(s): ")
                print()
                false = input("Enter Y to confirm details: ")

                if false.lower() == "Y":
                    break
                else:
                    print("Renter data")
                    print()
            print()

            room_l = [r1, r2 ,r3 ,r4]
            room_l2 = []
            for i in room_l:
                if i == '':
                    room_l2.append(0)
                else:
                    room_l2.append(int(i))
            print()
            cost = (room_l2[0] * 500) + (room_l2[1] * 650) + (room_l2[2] * 800) + (room_l2[3] * 1000)
            print(f"Total Cost: {cost}")
            print()
            money_g = int(input("Money Given: "))
            change = print(f"Change: {money_g - cost}")

            #create a list that contains [name, [room types], phone number]
            #put the cost in the sql file as well so its easy to add
            #store the amount of times each room is used
            for i in range(4): # [1,2,3,4]
                a = 0
                b = 0
                c = 0
                d = 0

                if i == 0:
                    while a < room_l2[i]:
                        cr.execute("select min(roomno) from rooms where guest is null and roomno between 1 and 40")
                        x = cr.fetchone()
                        x = int(x[0])

                        cr.execute(f"update rooms set guest = '{guest}', noguest = {guest_n}, phonenum = {pnum} where roomno = {x}")
                        cr.execute(f"update rooms set count = count + 1 where roomno = {x}")
                        a += 1
                        obj.commit()
                
                elif i == 1:
                    while b < room_l2[i]:
                        cr.execute("select min(roomno)from rooms where guest is null and roomno between 41 and 60 ")
                        x = cr.fetchone()
                        x = int(x[0])

                        cr.execute(f"update rooms set guest = '{guest}', noguest = {guest_n}, phonenum = {pnum} where roomno = {x}")
                        cr.execute(f"update rooms set count = count + 1 where roomno = {x}")
                        b += 1
                        obj.commit()

                elif i == 2:
                    while c < room_l2[i]:
                        cr.execute("select min(roomno) from rooms where guest is null and roomno between 61 and 70")
                        x = cr.fetchone()
                        x = int(x[0])

                        cr.execute(f"update rooms set guest = '{guest}', noguest = {guest_n}, phonenum = {pnum} where roomno = {x}")
                        cr.execute(f"update rooms set count = count + 1 where roomno = {x}")
                        c += 1
                        obj.commit()
                
                elif i == 3:
                    while d < room_l2[i]:
                        cr.execute("select min(roomno) from rooms where guest is Null and roomno between 71 and 75 ")
                        x = cr.fetchone()
                        x = int(x[0])

                        cr.execute(f"update rooms set guest = '{guest}', noguest = {guest_n}, phonenum = {pnum} where roomno = {x}")
                        cr.execute(f"update rooms set count = count + 1 where roomno = {x}")
                        d += 1
                        obj.commit()
            #To add the billing and stuff as well

        elif cho == "2":
            n = input("Enter the guest name to be removed: ")
            cr.execute(f"update rooms set guest = Null, noguest = 0, phonenum = Null where guest = '{n}' ")
            obj.commit()

        elif cho == "3":
            break

        else:
            print()
            print("Invalid Input. Only enter '1' or '2'")
            print()
