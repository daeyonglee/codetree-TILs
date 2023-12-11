a, b = input().split()
a, b = int(a), int(b)

start = a
end = b + 1
total = 0
if a > b:
    start = b
    end = a + 1

for i in range(start, end):
        if i % 5 == 0:
            total += i

print(total)