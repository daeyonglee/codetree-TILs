n = int(input())

count=1
for i in range(n, 0, -1):
    for j in range(count):
        print(j+i, end=" ")
    print()
    count+=1