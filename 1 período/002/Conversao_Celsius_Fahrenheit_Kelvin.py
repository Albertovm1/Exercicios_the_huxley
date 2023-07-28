Escala=input()
Temperatura=float(input())

C_K=Temperatura-273.15
F_K=((Temperatura-273.15)*1.8)+32
C_F=((Temperatura-32)/1.8)
K_F=((Temperatura-32)*(5/9)+273.15)
K_C=(Temperatura+273.15)
F_C=((Temperatura*1.8)+32)

if Escala=="K" or Escala=="k":
    if Temperatura<0.00:
        print("Valor de temperatura abaixo do minimo")
    else:
        print(f"%.2f C"%C_K)
        print(f"%.2f F"%F_K)

elif Escala=="F" or Escala=="f":
    if Temperatura<=(-459.67):
        print("Valor de temperatura abaixo do minimo")
    else:
        print(f"%.2f C"%C_F)
        print(f"%.2f K"%K_F)

elif Escala=="C" or Escala=="c":
    if Temperatura<=(-273.15):
        print("Valor de temperatura abaixo do minimo")
    else:
        print(f"%.2f F"%F_C)
        print(f"%.2f K"%K_C)