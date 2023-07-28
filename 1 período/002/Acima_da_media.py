numero_01=float(input())
numero_02=float(input())
numero_03=float(input())

media=(numero_01+numero_02+numero_03)/3

if media<numero_01 and media<numero_02 and media<numero_03:
    print("3")
elif media<numero_01 and media<numero_02 and media>numero_03:
    print("2")
elif media<numero_01 and media>numero_02 and media<numero_03:
    print("2")
elif media>numero_01 and media<numero_02 and media<numero_03:
    print("2")
elif media<numero_01 and media>numero_02 and media>numero_03:
    print("1")
elif media>numero_01 and media<numero_02 and media>numero_03:
    print("1")
elif media>numero_01 and media>numero_02 and media<numero_03:
    print("1")
else:
    print("0")