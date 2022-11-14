from Earnings import earning
from Employees import employee

def manager():
    while True:
        print("""
        Choose an option
        a) Employee Fuctions
        b) Room records
        c) Exit
        """)

        cho = input("Enter the option here: ").lower()

        if cho == "a":
            employee()
        
        elif cho == "b":
            print()
            earning()

        elif cho == "c":
            break

        else:
            print()
            print("Invalid Input")
