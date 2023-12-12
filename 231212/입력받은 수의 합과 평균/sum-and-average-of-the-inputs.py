n = int(input())

total = 0
for i in range(1, n+1):
    sin = int(input())
    total += sin

print(f"{total} {round(total/n, n)}")