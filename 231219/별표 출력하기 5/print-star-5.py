n = int(input())



for k in range(n, 0, -1):
    for i in range(k):
        for j in range(k):
            print("*", end="")
        print("", end=" ")
    print("")