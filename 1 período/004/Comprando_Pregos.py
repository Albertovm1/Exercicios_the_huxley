total_pregos = 0
while True:
    pregos = int (input())
    if pregos % 2 == 1:
        break
    total_pregos += pregos
quantidade_caixas = (total_pregos//12) + 1
valor_total = quantidade_caixas * 7.89
sobra = (quantidade_caixas*12) - total_pregos
print("{:.2f}".format(valor_total))
print(sobra)