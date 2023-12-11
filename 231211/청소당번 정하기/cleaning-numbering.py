n = int(input())

inside_clean = 0
center_clean = 0
toilet_clean = 0

for i in range(n):
    if i == 0:
        continue
    
    if i % 12 == 0:
        toilet_clean += 1
        continue
    if i % 3 == 0:
        center_clean += 1
        continue
    if i % 2 == 0:
        inside_clean += 1
        continue

print(f"{inside_clean} {center_clean} {toilet_clean}")