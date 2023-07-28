forma_geometrica= input()

if not (forma_geometrica=="Q" or forma_geometrica=="R" or forma_geometrica=="C"):
    print("Nenhuma figura selecionada")

if forma_geometrica== ("Q"):
    tamanho_lado= float(input())
    area_quadrado= tamanho_lado**2
    perimetro_quadrado= tamanho_lado*4
    print("{:.2f}".format(area_quadrado))
    print("{:.2f}".format(perimetro_quadrado))
    
elif forma_geometrica== ("R"):
    tamanho_altura= float(input())
    tamanho_largura= float(input())
    area_retangulo= tamanho_altura*tamanho_largura
    perimetro_retangulo= (tamanho_altura*2)+(tamanho_largura*2)
    print("{:.2f}".format(area_retangulo))
    print("{:.2f}".format(perimetro_retangulo))

elif forma_geometrica== ("C"):
    tamanho_raio= float(input())
    area_circulo=3.14*(tamanho_raio**2)
    comprimento_circulo=2*3.14*tamanho_raio
    print("{:.2f}".format(area_circulo))
    print("{:.2f}".format(comprimento_circulo))