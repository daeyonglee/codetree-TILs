result = True
for i in range(5):
    num = int(input())
    if num % 3 != 0:
        result = False

print(1) if result else print(0)