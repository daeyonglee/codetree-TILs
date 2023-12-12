a, b = input().split()
a, b = int(a), int(b)

total = 1
for i in range(a, b+1):
    total *= i

print(total)