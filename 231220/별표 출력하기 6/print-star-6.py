n = int(input())

col = n * 2 - 1

for i in range(col, 0, -2):
    empty_count = (col - i) // 2
    for _ in range(empty_count):
        print(" ", end=" ")
    for j in range(i):
        print("*", end=" ")
    for _ in range(empty_count):
        print(" ", end=" ")
    print("")
for i in range(3, col+1, 2):
    empty_count = (col - i) // 2
    for _ in range(empty_count):
        print(" ", end=" ")
    for j in range(i):
        print("*", end=" ")
    for _ in range(empty_count):
        print(" ", end=" ")
    print("")