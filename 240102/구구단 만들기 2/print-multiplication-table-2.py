a, b = tuple(map(int, input().split()))

for i in range(2,9, 2):
    start = a
    for j in range(b, a-1, -1):
        if j == a:
            print(f"{j} * {i} = {i*j}", end=" ")
        else:
            print(f"{j} * {i} = {i*j}", end=" / ")
    print()