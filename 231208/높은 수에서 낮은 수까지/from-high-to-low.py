a, b = input().split()
a = int(a)
b = int(b)

if a > b:
    i = a
    while i >= b:
        print(i, end=" ")
        i-=1
else:
    i = b
    while i >= a:
        print(i, end=" ")
        i-=1