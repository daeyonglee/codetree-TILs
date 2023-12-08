# 1 ~ n 확인
# 2의 배수 or 3의 배수 = 1
# not = 0
# 공백을 사이에 두고 출력

n = int(input())


for i in range(1, n+1):
    if i % 2 == 0 or i % 3 == 0:
        print(1, end=" ")
    else:
        print(0, end=" ")