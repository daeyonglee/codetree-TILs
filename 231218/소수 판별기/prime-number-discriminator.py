n = int(input())

isOk = True
for i in range(n):
    if i == 0 or i == 1:
        continue
    if n % i == 0:
        isOk = False
        break

print("P") if isOk else print("C")