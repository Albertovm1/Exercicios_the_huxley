def calcular_distancia(ponto_encontro, posicoes):
    soma_distancias = 0
    for posicao in posicoes:
        soma_distancias += abs(posicao - ponto_encontro)
    return soma_distancias
def encontrar_ponto_encontro(n, posicoes):
    menor_distancia = float('inf')
    ponto_encontro = -1
    for i in range(1, 1001):
        distancia = calcular_distancia(i, posicoes)
        if distancia < menor_distancia:
            menor_distancia = distancia
            ponto_encontro = i
    
    return menor_distancia, ponto_encontro
n = int(input())
posicoes = list(map(int, input().split()))
distancia, ponto_encontro = encontrar_ponto_encontro(n, posicoes)
print(distancia, ponto_encontro)
