n = int(input())
loop = 0
while True:
    if n == 1:
        if loop == 0:
            n = 0
        break
    
    if n % 2 == 0:
        n = n // 2
    elif n % 2 != 0:
        n = n * 3 + 1
    loop += 1

print(loop)