sum_age = 0
sum_person = 0
while True:
    age = int(input())
    if 20 <= age and 30 > age:
        sum_age += age
        sum_person += 1
    else:
        if sum_person == 0:
            print(0)
        else:
            print(format(round(sum_age / sum_person, 2), ".2f"))
        break