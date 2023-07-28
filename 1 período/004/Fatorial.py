while True:
    num = int (input())
    resultado = 1
    for i in range(1, num + 1):
        resultado *= i
    if num == -1:
        break
    print(resultado)