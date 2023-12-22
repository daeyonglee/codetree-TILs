n = int(input())

col_row = 2 * n + 1

for i in range(1, col_row+1):
    for j in range(1, col_row+1):
        if i == 1 or i == col_row or i % 2 != 0:
            print("* ", end="")
        else:
            if j % 2 != 0:
                print("* ", end="")
            else:
                print(" ", end=" ")
    print()