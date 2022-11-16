from Earnings import earning
from Employees import employee
from time import sleep

def manager():
    
    while True:
        print("""
        Choose an option
        a) Employee Functions
        b) Room records
        c) Exit
        """)

        cho = input("Enter the option here: ").lower()

        if cho == "a":
            employee()
            sleep(2)

        elif cho == "b":
            print()
            earning()
            sleep(2)

        elif cho == "c":
            break

        else:
            print()
            print("Invalid Input")
            sleep(2)
