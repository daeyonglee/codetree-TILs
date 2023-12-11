n = int(input())

total = 0
for i in range(1, n+1):
    sin = int(input())
    if sin % 2 != 0 and sin % 3 == 0:
        total += sin

print(total)