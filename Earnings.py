import matplotlib.pyplot as mpl

c1 = 20
c2 = 20
c3 = 20
c4 = 20

print(f"Number of Standard Room: {c1}")
print(f"Number of Superior Room: {c2}")
print(f"Number of Executive Rooms: {c3}")
print(f"Number of Presidential: {c4}")


colors = ["red", "orange", "yellow", "lightskyblue"]


mpl.pie([c1, c2, c3, c4], labels = ["Standard Rooms", "Superior Rooms", "Executive Rooms", "Presidential Suites"], colors = colors)

mpl.show()
