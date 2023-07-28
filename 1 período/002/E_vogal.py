letra= input()
vogal= ["A", "a", "E", "e", "I", "i", "O", "o", "U", "u"]

if len(letra) > 1: 
    print("1 caractere, por favor!")

elif letra in vogal:
        print("Eh vogal")

else:
    print("Nao eh vogal")