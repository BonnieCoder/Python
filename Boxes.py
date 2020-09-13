a1, b1, c1 = int(input()), int(input()), int(input())
a2, b2, c2 = int(input()), int(input()), int(input())

if (a1 > b1) and (b1 > c1):
    x1, y1, z1 = a1, b1, c1
elif (a1 > c1) and (c1 > b1):
    x1, y1, z1 = a1, c1, b1
elif (b1 > a1) and (a1 > c1):
    x1, y1, z1 = b1, a1, c1
elif (b1 > c1) and (c1 > a1):
    x1, y1, z1 = b1, c1, a1
elif (c1 > a1) and (a1 > b1):
    x1, y1, z1 = c1, a1, b1
else:
    x1, y1, z1 = c1, b1, a1

if (a2 > b2) and (b2 > c2):
    x2, y2, z2 = a2, b2, c2
elif (a2 > c2) and (c2 > b2):
    x2, y2, z2 = a2, c2, b2
elif (b2 > a2) and (a2 > c2):
    x2, y2, z2 = b2, a2, c2
elif (b2 > c2) and (c2 > a2):
    x2, y2, z2 = b2, c2, a2
elif (c2 > a2) and (a2 > b2):
    x2, y2, z2 = c2, a2, b2
else:
    x2, y2, z2 = c2, b2, a2

if (x1 == x2) and (y1 == y2) and (z1 == z2):
    print("Boxes are equal")
elif (x1 >= x2) and (y1 >= y2) and (z1 >= z2):
    print("The first box is larger than the second one")
elif (x1 <= x2) and (y1 <= y2) and (z1 <= z2):
    print("The first box is smaller than the second one")
else:
    print("Boxes are incomparable")
