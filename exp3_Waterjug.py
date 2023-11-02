def pour(jug1, jug2, max1, max2, fill):
    print("%d\t%d" % (jug1, jug2))
    if jug2 == fill:
        return
    elif jug2 == max2:
        pour(0, jug1, max1, max2, fill)
    elif jug1 != 0 and jug2 == 0:
        pour(0, jug1, max1, max2, fill)
    elif jug1 == fill:
        pour(jug1, 0, max1, max2, fill)
    elif jug1 < max1:
        pour(max1, jug2, max1, max2, fill)
    elif jug1 < (max2 - jug2):
        pour(0, (jug1 + jug2), max1, max2, fill)
    else:
        pour(jug1 - (max2 - jug2), (max2 - jug2) + jug2, max1, max2, fill)

print("Enter capacities of the jugs:")
max1 = int(input("Capacity of jug 1: "))
max2 = int(input("Capacity of jug 2: "))
fill = int(input("Target amount to be measured: "))

print("\n--------------------------")

print("JUG1\tJUG2")
pour(0, 0, max1, max2, fill)
