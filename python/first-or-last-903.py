list = list(map(int,str(input())))

if list[0] > list[-1]:
    print(list[0])
elif list[0] < list[-1]:
    print(list[-1])
elif list[0] == list[-1]:
    print("=")
