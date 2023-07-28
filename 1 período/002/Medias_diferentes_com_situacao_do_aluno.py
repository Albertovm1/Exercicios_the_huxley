tipo_nota=input()

if not (tipo_nota=="a" or tipo_nota== "p" or tipo_nota=="h"):
    print("Escolha um tipo de media valida.")

if tipo_nota==("a"):
    nota_01=float(input())
    nota_02=float(input())
    nota_03=float(input())
    m_a=(nota_01+nota_02+nota_03)/3
    if m_a>=70:
        print("{:.2f}".format(m_a))
        print("Aprovado")
    elif m_a>0 and m_a<40:
        print("{:.2f}".format(m_a))
        print("Reprovado")
    elif m_a>40 and m_a<70:
        print("{:.2f}".format(m_a))
        print("Final")
    else:
        print("Media invalida")

if tipo_nota==("p"):
    nota_01=float(input())
    nota_02=float(input())
    nota_03=float(input())
    peso_01=float(input())
    peso_02=float(input())
    peso_03=float(input())
    m_p=(nota_01*peso_01+nota_02*peso_02+nota_03*peso_03)/(peso_01+peso_02+peso_03)
    if m_p>=70:
        print("{:.2f}".format(m_p))
        print("Aprovado")
    elif m_p>0 and m_p<40:
        print("{:.2f}".format(m_p))
        print("Reprovado")
    elif m_p>40 and m_p<70:
        print("{:.2f}".format(m_p))
        print("Final")
    else:
        print("Media invalida")

if tipo_nota==("h"):
    nota_01=float(input())
    nota_02=float(input())
    nota_03=float(input())    
    m_h=3/((1/nota_01)+(1/nota_02)+(1/nota_03))
    if m_h>=70:
        print("{:.2f}".format(m_h))
        print("Aprovado")
    elif m_h>0 and m_h<40:
        print("{:.2f}".format(m_h))
        print("Reprovado")
    elif m_h>40 and m_h<70:
        print("{:.2f}".format(m_h))
        print("Final")
    else:
        print("Media invalida")