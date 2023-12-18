n = int(input())
x = 0


while True:
    if n == 2 ** x:
        n = 2 ** x
        break
    x += 1

print(x)