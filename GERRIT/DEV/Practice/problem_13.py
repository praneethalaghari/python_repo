def generatefibanocciseries(msg = "Enter number of finbanocci series :"):
    n = int(input(msg))
    i = 0
    f1 = 0
    f2 = 1

    while (i+1<n):
        if (i == 0):
            print(f1, f2)
            i+= 1
            continue
        i+= 1
        f3 = f1 + f2
        f1 = f2
        f2 = f3
        print(f3)


generatefibanocciseries()