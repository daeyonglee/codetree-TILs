c, n = input().split()
n = int(n)

if c == "A":
    for i in range(1, n+1):
        print(i, end=" ")
if c == "D":
    for j in range(n+1, 1, -1):
        print(j, end=" ")