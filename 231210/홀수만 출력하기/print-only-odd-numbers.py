line = int(input())

result = list()
for i in range(line):
    a = int(input())
    if a % 3 == 0 and a % 2 != 0:
        result.append(a)

for j in result:
    print(j)