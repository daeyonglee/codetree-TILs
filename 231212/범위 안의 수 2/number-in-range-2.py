total = 0
count = 0
for i in range(10):
    sin = int(input())
    if sin > 0 and sin <= 200:
        total += sin
        count += 1

print(f"{total} {round(total/count, 1)}")