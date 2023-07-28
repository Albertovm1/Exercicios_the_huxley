dias=int(input())
km=int(input())
taxa=12*(km-(100*dias))

valor_pago=(90*dias)+taxa
valor_pago_02=90*dias

if km==(dias*100) or km<100:
    print("{:.2f}".format(valor_pago_02))

else:
    print("{:.2f}".format(valor_pago))