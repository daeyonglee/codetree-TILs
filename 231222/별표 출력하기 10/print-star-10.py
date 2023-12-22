n = int(input())

for i in range(1, n+1):
    reverse_col = n - i + 1
    for j in range(1, i+1, 1):
        print("* ", end="")
    print()
    for k in range(reverse_col, 0, -1):
        print("* ", end="")
    print()