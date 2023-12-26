n = int(input())

for i in range(1, n+1):
    start_value = i * n
    for j in range(n):
        print(start_value - j * i, end=" ")
    print()