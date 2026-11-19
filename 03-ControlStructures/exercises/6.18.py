###
# Program określa położenie punktu P(x, y) w układzie współrzędnych (ćwiartka, oś lub początek układu).
#

x = int(input("Enter x: "))
y = int(input("Enter y: "))

# Określenie położenia punktu na podstawie wartości współrzędnych x oraz y
if x == 0 and y == 0:
    print(f"Point P({x},{y}) is at the origin (0,0)")
elif x == 0:
    print(f"Point P({x},{y}) is on the y-axis")
elif y == 0:
    print(f"Point P({x},{y}) is on the x-axis")
elif x > 0 and y > 0:
    print(f"Point P({x},{y}) is in the first quadrant of the coordinate system")
elif x < 0 and y > 0:
    print(f"Point P({x},{y}) is in the second quadrant of the coordinate system")
elif x < 0 and y < 0:
    print(f"Point P({x},{y}) is in the third quadrant of the coordinate system")
else:
    print(f"Point P({x},{y}) is in the fourth quadrant of the coordinate system")