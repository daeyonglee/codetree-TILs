a,b = input().split()
a = int(a)
b = int(b)

for i in range(a, b-2, -2):
    print(a, end=" ")
    a -= 2