n = int(input())

for i in range(1, n+1):
    num = 2 * i + 9
    for _ in range(n):
        print(num, end=" ")
        num += 2
    print()