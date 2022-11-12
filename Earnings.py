import matplotlib.pyplot as mpl
import mysql.connector as mql

def earning():
    obj = mql.connect(host = "localhost", user = "root", passwd = "hayden", database = "hotel")

    cr = obj.cursor()

    #import this from the sql file
    #better to import each sperately, else a list
    #sum of the worker salaries
    cr.execute("select sum(count) from rooms where roomno between 1 and 40")
    a = cr.fetchone()
    print(f"Number of Standard Room: {a[0]}")

    cr.execute("select sum(count) from rooms where roomno between 41 and 60")
    b = cr.fetchone()
    print(f"Number of Superior Room: {b[0]}")

    cr.execute("select sum(count) from rooms where roomno between 61 and 70")
    c = cr.fetchone()
    print(f"Number of Executive Rooms: {c[0]}")

    cr.execute("select sum(count) from rooms where roomno between 61 and 70")
    d = cr.fetchone()
    print(f"Number of Presidential: {d[0]}")


    colors = ["red", "orange", "yellow", "lightskyblue"]


    mpl.pie([a, b, c, d], labels = ["Standard Rooms", "Superior Rooms", "Executive Rooms", "Presidential Suites"], colors = colors)

    mpl.show()
