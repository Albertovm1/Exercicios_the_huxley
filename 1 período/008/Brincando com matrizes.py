def calculo_media ():
    soma = sum(valores)
    media = soma / len(valores)
    return media

def maior_valor ():
    maior_v = max (valores)
    return maior_v

def valor_delta ():
    if m_v > 0:
        delta = 1
    elif m_v < 0:
        delta = -1
    elif m_v == 0:
        delta = 0
    return delta

def s_diagonal_principal():
    soma = 0
    for i in range(len(valores)):
        if i % 4 == 0:
            soma += valores[i]
    return soma

valores = []
soma = 0
for i in range(9):
    valor = int(input())
    valores.append(valor)
    soma += valor

m = calculo_media()
m_v = maior_valor()
d = valor_delta()
s_d = s_diagonal_principal()
print ("{:.2f} {} {} {}".format(m, m_v, d, s_d))