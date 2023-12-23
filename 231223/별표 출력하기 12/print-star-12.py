n = int(input())

for i in range(n, 0, -1):
    empty_count = n - i
    for j in range(empty_count):
        print(" ", end=" ")
    for k in range(i, 0, -1):
        if n % 2 == 0:
            if n == i:
                print("*", end=" ")
            elif k % 2 == 0:
                print(" ", end=" ")
            else:
                print("*", end=" ")
        else:
            if n == i:
                print("*", end=" ")
            elif k % 2 != 0:
                print(" ", end=" ")
            else:
                print("*", end=" ")
    print()