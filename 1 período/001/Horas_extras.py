SALARIO_BASE=float(input())
HORA_EXTRA=int(input())

VALOR_HORA= SALARIO_BASE/44
SALARIO_FINAL=((VALOR_HORA+(VALOR_HORA*0.1))*HORA_EXTRA)+SALARIO_BASE

print("{:.2F}".format(SALARIO_FINAL))
