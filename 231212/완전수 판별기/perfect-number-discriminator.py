n = int(input())

total = 0

for i in range(1, n):
    if n % i == 0:
        total += i

if n == total:
    print("P")
else:
    print("N")