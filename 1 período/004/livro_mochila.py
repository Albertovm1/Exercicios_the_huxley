capacidade = 18
quantidade = 0
peso_total = 0
while True:
    peso = float(input())
    if peso_total + peso < capacidade:
        peso_total += peso
        quantidade += 1
    else:
        break
print(quantidade)