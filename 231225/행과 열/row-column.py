row, col = list(map(int, input().split()))

for i in range(1, row+1):
    for j in range(1, col+1):
        print(i*j, end=" ")
    print()