n = int(input())

for i in range(1, n+1):
    reverse_col = n - i + 1
    for k in range(reverse_col, 0, -1):
        print("* ", end="")
    print()
    for j in range(0, i, 1):
        print("* ", end="")
    print()