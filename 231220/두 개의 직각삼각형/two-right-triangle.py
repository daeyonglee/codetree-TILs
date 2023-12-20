n = int(input())

col = n * 2
empty_col = 0

for i in range(col, 0, -2):
    star_count = i // 2
    empty_count = empty_col * 2
    for _ in range(star_count):
        print("*", end="")
    for j in range(empty_count):
        print(" ", end="")
    for _ in range(star_count):
        print("*", end="")
    empty_col += 1
    print("")