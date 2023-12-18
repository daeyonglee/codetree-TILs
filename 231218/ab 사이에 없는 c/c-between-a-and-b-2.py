a, b, c = input().split()
a, b, c = int(a), int(b), int(c)

result = False
for i in range(a, b+1):
    if i % c == 0:
        result = True
        break

print("NO") if result else print("YES")