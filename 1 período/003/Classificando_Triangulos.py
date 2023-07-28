def tipo_triangulo(lado, lado_2, lado_3):
    if lado < (lado_2+lado_3):
        if (lado == lado_2 == lado_3):
            return ("EQUILATERO")
        elif lado_2 == lado_3:
            return("ISOSCELES")
        elif (lado != lado_2 != lado_3):
            return("ESCALENO")
    else:
        return("INVALIDO")

while True:
    entrada = input().split()
    if entrada[0] == "FIM":
        break
    lado, lado_2, lado_3 = map(int, entrada)
    tipo = tipo_triangulo(lado, lado_2, lado_3)
    print(tipo)