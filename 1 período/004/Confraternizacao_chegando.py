valor_total = float(input())
num_sindicalistas = int(input())
soma_valores_pagos = 0
maior_valor_pago = 0
nome_maior_valor_pago = ""
for i in range(num_sindicalistas):
    nome = input()
    valor_pago = float(input())
    soma_valores_pagos += valor_pago
    if valor_pago > maior_valor_pago:
        maior_valor_pago = valor_pago
        nome_maior_valor_pago = nome
if num_sindicalistas == 0:
    print("Nao ha conta ou funcionario suficiente para pagar a conta")
elif soma_valores_pagos > valor_total:
    media = soma_valores_pagos / num_sindicalistas
    excedente = soma_valores_pagos - valor_total
    print("{} pagou R$ {:.1f}".format(nome_maior_valor_pago, maior_valor_pago))
    print("Valor excedente: sobra R$  {:.1f}".format(excedente))
else:
    saldo_neg = valor_total - soma_valores_pagos
    print("{} pagou R$ {:.1f}".format(nome_maior_valor_pago, maior_valor_pago))
    print("Valor insuficiente: falta R$  {:.1f}".format(saldo_neg))