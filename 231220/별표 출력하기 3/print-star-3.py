n = int(input())

col = n * 2 - 1
empty_col = 0
for i in range(col, 0, -2):
    for k in range(empty_col):
        print(" ", end=" ")
    for j in range(i):
        print("*", end=" ")
    for kk in range(empty_col):
        print(" ", end=" ")
    print("")
    empty_col += 1