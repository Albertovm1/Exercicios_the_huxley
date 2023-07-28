def inversor_texto (texto): 
    palavras = texto.split()  
    palavras_invertidas = [] 
    contador = 1
    for palavra in palavras:
        if contador % 2 == 0:
            palavra_invertida = palavra [::-1]
            print(palavra_invertida)
            palavras_invertidas.append (palavra_invertida)
        else:
            palavras_invertidas.append(palavra) 
        contador += 1
    
    texto_invertido = ' '.join(palavras_invertidas) 
    return texto_invertido         
texto_entrada = input()
texto_saida = inversor_texto(texto_entrada)
print(texto_saida)