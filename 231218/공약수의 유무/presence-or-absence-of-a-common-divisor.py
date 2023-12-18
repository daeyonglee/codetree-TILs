a, b = input().split()
a, b = int(a), int(b)

result = False
for i in range(a, b+1):
    if 1920 % i == 0 and 2880 % i == 0:
        result = True
        break

print(1) if result else print(0)