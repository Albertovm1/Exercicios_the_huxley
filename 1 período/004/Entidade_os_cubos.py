n = int(input())
altura = 0
cubos_resto = n 
while cubos_resto >= 0:
    altura +=1
    cubos_necessario = altura*(altura+1)/2
    cubos_resto -= cubos_necessario
print(altura-1)