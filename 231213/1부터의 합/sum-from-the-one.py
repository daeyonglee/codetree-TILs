n = int(input())

total = 0
for i in range(1, 101):
    total += i
    if n <= total+i:
        print(total)
        break