n = int(input())

if (n >= 1 and n <= 3):
    print("Initial")
elif (n >= 3 and n <=6):
    print("Average")
elif (n >= 7 and n <= 9):
    print("Sufficient")
elif (n >= 10 and n <= 12):
    print("High")
else:
    print("Error!")
