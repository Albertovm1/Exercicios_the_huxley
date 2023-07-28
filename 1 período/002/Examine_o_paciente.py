Sua_temperatura=float(input())
Secrecao=input()

if not Secrecao==("N") and not Secrecao==("S"):
    print("Erro")
else:
    if Sua_temperatura>=37 and Secrecao==("S"):
        print("Exames Especiais")
if Sua_temperatura>=37 and Secrecao==("N"):
    print("Exames Basicos")
if Sua_temperatura<37 and Secrecao==("N"):
    print("Liberado")
if Sua_temperatura<37 and Secrecao==("S"):
    print("Exames Basicos")