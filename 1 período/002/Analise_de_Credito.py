salario=float(input())
valor_comprometido =float(input())

limite_comprometimento=salario*0.3
limite_disponível=salario-(salario*0.7)-valor_comprometido

if valor_comprometido<limite_comprometimento:
    print("{:.2f}".format(limite_disponível))
elif valor_comprometido>limite_comprometimento:
    print("{:.2f}".format(salario-salario))