arr = list()
three_count = 0
five_count = 0

for i in range(10):
    sin = int(input())
    arr.append(sin)

for i in arr:
    if i % 3 == 0:
        three_count += 1
    if i % 5 == 0:
        five_count += 1

        
print(f"{three_count} {five_count}")