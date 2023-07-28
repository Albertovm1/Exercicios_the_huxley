def multiplicador_diagonalP(matriz, k):
    for i in range(len(matriz)):
        matriz[i][i] *= k

def imprimir(linha):
    for elemento in linha:
        print(elemento, end=' ')
    print()

def matriz_4():
    matriz = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
    for i in range(4):
        for j in range(4):
            n = int(input())
            matriz[i][j] = n
    return matriz

while True:
    k = int(input())
    if k == 0:
        break
    matriz = matriz_4()
    multiplicador_diagonalP(matriz, k)
    transposed_matriz = [[matriz[j][i] for j in range(len(matriz))] for i in range(len(matriz[0]))]
    for linha in transposed_matriz:
        imprimir(linha)