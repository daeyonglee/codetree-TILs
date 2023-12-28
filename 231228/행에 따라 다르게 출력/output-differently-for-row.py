n = int(input())

start = 1
end = n + 1
for i in range(1,n+1):
    step = 2 if i % 2 == 0 else 1
    for j in range(start, end, step):
        print(j, end=" ")
    start = end if i % 2 == 0 else end + 1
    end = end + n  if i % 2 == 0 else end + n*2
    print()