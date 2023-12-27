n = int(input())

for i in range(1, n+1):
    start = [n, 0, -1] if i % 2 == 0 else [1, n+1, 1]
    for j in range(start[0], start[1], start[2]):
        print(j, end="")
    print()