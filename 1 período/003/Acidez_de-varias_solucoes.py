while True:
    ph_valor =float(input())
    if ph_valor == -1:
        break
    if ph_valor < 7:
        print("ACIDA")
    elif ph_valor == 7:
        print("NEUTRA")
    else:
        print("BASICA")