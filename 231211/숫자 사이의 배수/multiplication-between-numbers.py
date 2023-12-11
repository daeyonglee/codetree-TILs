a, b = input().split()
a, b = int(a), int(b)

total = 0
count = 0
for i in range(a, b+1):
    if i % 5 == 0 or i % 7 == 0:
        total += i
        count += 1

print (f"{total} {round(total/count, 1)}")