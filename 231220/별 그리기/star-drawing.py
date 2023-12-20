n = int(input())
empty_count = n-1
for i in range(1, n+1):
    col = i * 2 - 1
    for _ in range(empty_count):
        print(" ", end="") 
    for _ in range(col):
        print("*", end="")
    for _ in range(empty_count):
        print(" ", end="")
    print("")
    empty_count -= 1
empty_count = 1    
for i in range(n-1, 0, -1):
    col = i * 2 - 1
    for _ in range(empty_count):
        print(" ", end="") 
    for _ in range(col):
        print("*", end="")
    for _ in range(empty_count):
        print(" ", end="")
    print("")
    empty_count += 1