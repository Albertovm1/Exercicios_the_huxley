def ehbissexto (ano):
    if ano % 4 != 0:
        return False
    elif ano % 100 != 0:
        return True
    elif ano % 400 != 0:
        return False
    else:
        return True 
def contaDigitos (ano):
    quantidade_digitos = len(str(ano))
    if quantidade_digitos == 4:
        return True
    else:
        return False
ano = input().split()
for ano_str in ano:
    ano = int(ano_str)
    if contaDigitos(ano) == True:
        if ehbissexto(ano) == True:
            if ano == 2020:
                print ("O ano {} eh bissexto".format(ano))
            elif ano < 2020:
                print ("O ano {} foi bissexto".format(ano))
            elif ano > 2020:
                print ("O ano {} serah bissexto".format(ano))
        else:
            print ("O ano {} NAO eh bissexto".format(ano))
    else:
        print ("Ano invalido")