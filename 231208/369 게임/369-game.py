# input ; 자연수 n
# 1 ~ n까지
# 369게임을 진행하여 출력
# 조건 1. 3의배수 or 숫자에 3,6,9 중 하나가 포함되어 있을 경우 -> 0 출력 아니면 그 숫자 그대로 출력


def isIncludeThreeSixNine(value):
    if str(value).find("3") != -1 or str(value).find("6") != -1 or str(value).find("9") != -1:
        return True
    return False

n = int(input())

for i in range(1, n+1):
    isOk = isIncludeThreeSixNine(i)

    if i % 3 == 0 or isOk:
        print(0, end=" ")
    else:
        print(i, end=" ")