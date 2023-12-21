n = int(input())

empty_count = n - 1

for i in range(1, n+1):
    alpha_count = n - empty_count
    for _ in range(empty_count):
        print(" ", end=" ")
    for j in range(alpha_count):
        print("@", end=" ")
    print()
    empty_count -= 1

empty_count = 1
for i in range(n, 0, -1):
    alpha_count = n - empty_count
    for j in range(alpha_count):
        print("@", end=" ")
    for _ in range(empty_count):
        print(" ", end=" ")
    print()
    empty_count += 1