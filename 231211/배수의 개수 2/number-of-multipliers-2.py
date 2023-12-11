# 10개 숫자 중 홀수의 갯수를 출력

arr = list()
count = 0

for i in range(10):
   sin = int(input())
   arr.append(sin)

for i in arr:
    if i % 2 != 0:
        count += 1

print(count)