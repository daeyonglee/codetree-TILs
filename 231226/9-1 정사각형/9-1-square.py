n = int(input())

value = 9
for i in range(1, n+1):
    for j in range(1, n+1):
        print(value, end="")
        if value != 1:
            value -= 1
        else:
            value = 9
    print()