n = int(input())

total = 0
for i in range(1, 101):
    if n <= total+i:
        print(i)
        break
    total += i