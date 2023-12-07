a, b = input().split()
a = int(a)
b = int(b)


print(f'{a//b}.', end='')

a %= b

for _ in range(20):
    a  *= 10
    print(a//b, end='')
    a %= b