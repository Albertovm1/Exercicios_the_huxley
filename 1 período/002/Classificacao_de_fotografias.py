psrn=float(input())
analise_enquadramento=input()
exposicao=input()

if psrn>=80 and psrn<=90: 
    if (analise_enquadramento=="bom" or  analise_enquadramento=="excelente") and exposicao=="bem exposta":
        print("para imprimir")
    elif (analise_enquadramento=="bom" or  analise_enquadramento=="excelente") and (exposicao=="subexposta" or exposicao=="superexposta"):
        print("boa")
    else:
        print("marromeno")
if psrn>=50 and psrn<80:
    if analise_enquadramento=="excelente" and exposicao=="bem exposta":
        print("boa")
    else:
        print("marromeno")
if psrn<50:
    if analise_enquadramento=="excelente" and exposicao=="bem exposta":
        print("marromeno")
    else:
        print("lixo")