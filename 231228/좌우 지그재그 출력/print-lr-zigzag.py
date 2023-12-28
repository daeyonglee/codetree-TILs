n = int(input())

for i in range(1,n+1):
    start = n * i if i % 2 == 0 else n*(i-1) + 1
    end = n*i-n if i % 2 == 0 else n*i + 1
    step = -1 if i % 2 == 0 else 1
    # 1 => 1
    # 2 => 8
    # 3 => 9 
    for j in range(start, end, step):
        print(j, end=" ")
    print()