# 정수 a ~ b까지 출력
# start ; a
# end ; > b
# 1. 홀수일경우 2배
# 2. 짝수인 경우 +3

a, b = input().split()
a = int(a)
b = int(b)

result = a
while result <= b:
    print(result, end=" ")
    if result % 2 != 0:
        result *= 2
    elif result %2 == 0:
        result += 3
    else:
        result += 1