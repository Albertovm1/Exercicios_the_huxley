import math
meta = 0
soma = 0
quantidade = 0
for i in range(7):
    correspondecias_entregues = int (input())
    quantidade += 1 
    soma += correspondecias_entregues
    media = soma/quantidade
    if correspondecias_entregues >= 100:
        meta += 1
print(meta)
print(round(media))