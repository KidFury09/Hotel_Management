import matplotlib.pyplot as mpl
import mysql.connector as mql

def earning():
    obj = mql.connect(host = "localhost", user = "root", passwd = "hayden", database = "hotel")

    cr = obj.cursor()

    cr.execute("select sum(count) from rooms where roomno between 1 and 40")
    a = cr.fetchone()
    a = int(a[0])    
    print(f"Number of Standard Room: {a}")

    cr.execute("select sum(count) from rooms where roomno between 41 and 60")
    b = cr.fetchone()
    b = int(b[0])
    print(f"Number of Superior Room: {b}")

    cr.execute("select sum(count) from rooms where roomno between 61 and 70")
    c = cr.fetchone()
    c = int(c[0])
    print(f"Number of Executive Rooms: {c}")

    cr.execute("select sum(count) from rooms where roomno between 71 and 75")
    d = cr.fetchone()
    d = int(d[0])
    print(f"Number of Presidential: {d}")

    colors = ["red", "orange", "yellow", "lightskyblue"]

    mpl.pie([a, b, c, d], labels = ["Standard Rooms", "Superior Rooms", "Executive Rooms", "Presidential Suites"], colors = colors)

    mpl.show()
