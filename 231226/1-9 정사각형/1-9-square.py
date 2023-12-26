n = int(input())

col = 1
for i in range(1, n+1):
    for j in range(1, n+1):
        print(col, end="")
        if col == 9:
            col = 1
        else:
            col += 1
    print()