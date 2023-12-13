n = int(input())

total = 1
for i in range(1, 11):
    if n <= total*i:
        print(i)
        break
    total *= i