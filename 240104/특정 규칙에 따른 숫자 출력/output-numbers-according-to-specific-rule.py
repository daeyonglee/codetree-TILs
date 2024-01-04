n = int(input())

count = 1
for i in range(n, 0, -1):
    for _ in range(n-i):
        print(" ",end=" ")
    for j in range(i):
        print(count, end=" ")
        if count == 9:
            count = 1
        else:
            count+=1
    print()