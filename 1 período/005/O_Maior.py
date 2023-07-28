def maior(a: int, b: int, s: int):
    maiorab = (a + b + abs(a - b)) // 2
    maiorab = (maiorab + c + abs(maiorab - c)) // 2
    return maiorab

a, b, c = map(int, input().split())
eh_maior = maior (a, b, c)
print ("{} eh o maior".format(eh_maior))