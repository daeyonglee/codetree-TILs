n = int(input())

col = 2
for i in range(1, n+1):
    
    for j in range(1, n+1):
        print(col, end=" ")
        if col != 8:
            col += 2
        else:
            col = 2
    print()