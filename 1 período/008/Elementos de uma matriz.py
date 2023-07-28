def criar_matriz(linhas, colunas):
    matriz = []
    for _ in range(linhas):
        linha = []
        for _ in range(colunas):
            elemento = int(input())
            linha.append(elemento)
        matriz.append(linha)
    return matriz

def imprimir_matriz(matriz):
    print("Matriz formada:")
    for linha in matriz:
        for elemento in linha:
            print(str(elemento).rstrip(), end=' ')
        print()

def diagonal_principal(matriz):
    if len(matriz) != len(matriz[0]):
        return None
    soma = 0
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if i == j:
                soma += matriz[i][j]
    return soma

def diagonal_secundaria(matriz):
    if len(matriz) != len(matriz[0]):
        return None
    soma = 0
    for i in range(len(matriz)):
        j = len(matriz) - 1 - i
        soma += matriz[i][j]
    return soma

def menor_0(matriz):
    contador = 0
    for linha in matriz:
        for elemento in linha:
            if elemento < 0:
                contador += 1
    return contador

def maior_0(matriz):
    contador = 0
    for linha in matriz:
        for elemento in linha:
            if elemento > 0:
                contador += 1
    return contador

linhas, colunas = map(int, input().split())
matriz = criar_matriz(linhas, colunas)
imprimir_matriz(matriz)

soma_diagonal_principal = diagonal_principal(matriz)
soma_diagonal_secundaria = diagonal_secundaria(matriz)
if soma_diagonal_principal is not None and soma_diagonal_secundaria is not None:
    print("A diagonal principal e secundaria tem valor(es) {} e {} respectivamente."
          .format(soma_diagonal_principal, soma_diagonal_secundaria))
else:
    print("A diagonal principal e secundaria nao pode ser obtida.")

print("A matriz possui {} numero(s) menor(es) que zero.".format(menor_0(matriz)))
print("A matriz possui {} numero(s) maior(es) que zero.".format(maior_0(matriz)))