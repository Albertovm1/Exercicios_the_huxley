def calcular_numero_habitantes(pi, ai, q, af):
    habitantes = []
    for t in range(ai, af + 1):
        anos_passados = t - ai
        numero_habitantes = pi * (1 + q/100) ** anos_passados
        habitantes.append(numero_habitantes)
    return habitantes

populacao_i = int (input())
ano_i = int (input())
percentual_c = int (input())
ano_f = int (input())

habitantes_por_ano = calcular_numero_habitantes(populacao_i, ano_i, percentual_c, ano_f)

for i, habitantes in enumerate(habitantes_por_ano):
    ano = ano_i + i
    print ("{} {}".format (ano, round (habitantes)))