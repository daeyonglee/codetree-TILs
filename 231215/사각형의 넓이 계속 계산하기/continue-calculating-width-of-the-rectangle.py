while True:
    width, height, alphabet = input().split()
    width, height = int(width), int(height)

    print(width * height)

    if alphabet == "C":
        break