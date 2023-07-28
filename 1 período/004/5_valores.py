quantidade_neg = 0

for i in range(5):
    a = float(input("Digite um valor:\n"))
    if a < 0:
        quantidade_neg += 1
print ("Foram digitados", quantidade_neg, "numeros negativos\n")