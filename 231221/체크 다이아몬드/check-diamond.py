n = int(input())

total_col = 2 * n - 1
print_star_count = 1
for i in range(n, 0, -1):
    count = 0
    cursor = i
    for _ in range(i-1):
        print(" ", end="")
    for j in range(i, total_col+1):
        if print_star_count == count:
            break
        if j == cursor:
            print("*", end="")
            count += 1
            cursor += 2
        else:
            print(" ", end="")
    print_star_count += 1
    print()

print_star_count = n - 1
for i in range(2, n+1):
    count = 0
    cursor = i
    for _ in range(i-1):
        print(" ", end="")
    for j in range(i, total_col+1):
        if print_star_count == count:
            break
        if j == cursor:
            print("*", end="")
            count += 1
            cursor += 2
        else:
            print(" ", end="")
    print_star_count -= 1
    print()