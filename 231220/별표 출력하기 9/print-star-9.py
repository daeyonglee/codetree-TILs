n = int(input())

col = n * 2 - 1

for i in range(1, col+1, 2):
    empty_col = (col - i) // 2
    for _ in range(empty_col):
        print(" ", end=" ")
    for j in range(i):
        print("*", end=" ")
    for _ in range(empty_col):
        print(" ", end=" ")
    print("")