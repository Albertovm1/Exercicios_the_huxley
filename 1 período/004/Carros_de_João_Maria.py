quantidade_carros = 0
carro_mais_novo = 0
carro_mais_rapido = 0
velocidade_total = 0
i = 0
while True:
    play_stop = input()
    if play_stop == "N" or play_stop == "n":
        if i == 0:
            print("zero")
            exit()
        break
    i += 1
    ano = int (input())
    velocidade = float (input())
    quantidade_carros += 1
    velocidade_total += velocidade
    
    if ano > carro_mais_novo:
        carro_mais_novo = ano
        
    if velocidade > carro_mais_rapido:
        carro_mais_rapido = velocidade
if quantidade_carros > 0:
    velocidade_media = velocidade_total / quantidade_carros
else:
    velocidade_media = 0
print("{:.2f}".format(carro_mais_rapido))
print(carro_mais_novo)
print("{:.2f}".format (velocidade_media))