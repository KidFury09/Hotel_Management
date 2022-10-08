from matplotlib.pyplot import pie 

earnings = 0 #import this from the sql file
rooms = [] #better to import each sperately, else a list
salaries = 0 #sum of the worker salaries
c1 = 0
c2 = 0
c3 = 0
c4 = 0

print(f"Number of Standard Room: {c1}")
print(f"Number of Superior Room: {c2}")
print(f"Number of Executive Rooms: {c3}")
print(f"Number of Presidential: {c4}")
print()
print(f"Total income: {earnings}")
print()

size = [electric_cost, water_cost, salarier, maintanance]
labels = ["Electricity", "Water", "Salary", "Maintanace"]
colors = ["red", "orange", "yellow", "lightskyblue"]

pie(size, labels = labels, colors = colors)

pie([c1, c2, c3, c4], ["Standard Rooms", "Superior Rooms", "Executive Rooms", "Presidential Suites"], colors = colors)