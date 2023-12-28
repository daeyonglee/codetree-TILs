n = int(input())

odd = 1
even = n
for i in range(1, n+1):
    for j in range(1,n+1):
        print(even, end="") if j % 2 == 0 else print(odd, end="")
    odd += 1
    even -= 1
    print()