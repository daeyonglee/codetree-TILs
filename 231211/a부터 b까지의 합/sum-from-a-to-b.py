a, b = input().split()
a = int(a)
b = int(b)

total = 0
for i in range(a, b+1):
    total += i

print(total)