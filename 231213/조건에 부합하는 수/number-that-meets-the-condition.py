def condition1(i):
    return i % 2 == 0 and i % 4 != 0

def condition2(i):
    return (i // 8) % 2 == 0

def condition3(i):
    return i % 7 < 4



a = int(input())

for i in range(1, a + 1):
    if not condition1(i) and not condition2(i) and not condition3(i):
        print(i, end=" ")