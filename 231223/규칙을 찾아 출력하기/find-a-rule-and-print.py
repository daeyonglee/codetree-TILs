n = int(input())

star = 0
for i in range(1, n+1):
    for j in range(1, n+1):
        if i == 1 or i == n:
            print("*", end=" ")
        else:
            if j <= star or j == n:
                print("*", end=" ")
            else:
                print(" ", end=" ")
    star += 1
    print()