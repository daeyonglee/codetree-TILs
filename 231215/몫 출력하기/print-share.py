loop = 0

while loop < 3:
    number = int(input())
    if number % 2 == 0:
        print( number // 2)
    else:
        continue
    
    loop += 1