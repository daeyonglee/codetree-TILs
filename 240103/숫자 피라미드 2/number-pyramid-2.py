n = int(input())

start = 1
for i in range(1, n+1):
    start += i - 1
    for j in range(i):
        print(start+j, end=" ")
    print()