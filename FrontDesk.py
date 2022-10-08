print("""Please Chose An Option
1) Adding Guest
2) Removing Guest""")
print()

while True:
    cho = int(input("Enter your choice here: "))
    print()
    if cho == 1:
        guest = input("Customer name: " )
        pnum = input("Phone number: ")
        print()
        guest_n = int(input("Number of Guests: "))

        print()
        """
        c1 = 0
        c2 = 0
        c3 = 0
        c4 = 0
        while True:
            x = load()
            if x(Name) == null:
                if x(room) in range(1,41):
                    c1+=1
                elif x(room) in range(41, 61):
                    c2+=1
                elif x(room) in range(61,71):
                    c3+=1
                else:
                    c4+=1
        print('''Avaliable rooms
        Standard Rooms: {c1}
        Superior Rooms: {c2}
        Executive Rooms: {c3}
        Presidential Suite: {c4}
        ''')

        """
        

        print("Enter the room type below: ")
        print()
        r1 = input("Standard Room(s): ")
        r2 = input("Superior Room(s): ")
        r3 = input("Executive Room(s): ")
        r4 = input("Presidential Suite(s): ")

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
        money_g = int(input("Money Given:"))
        change = print(f"Change: {money_g - cost}")

        #create a list that contains [name, [room types], phone number]
        #put the cost in the sql file as well so its easy to add
        #store the amount of times each room is used
        break
        #To add the billing and stuff as well

    elif cho == 2:
        break #we need to learn the sql side for this

    else:
        print("Invalid Input. Only enter '1' or '2'")
        print()