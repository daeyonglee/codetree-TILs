# 90 >=   ; A
# 80 >=   ; B
# 70 >=   ; C
# 60 >=   ; D
# 60 <    ; F

# input ; n
# for n ~ 100
# ++

def grade(score) -> str:
    if score >= 90:
        return "A"
    if score >= 80:
        return "B"
    if score >= 70:
        return "C"
    if score >= 60:
        return "D"
    return "F"


n = int(input())

for i in range(n, 101, 1):
    print(grade(i), end=" ")