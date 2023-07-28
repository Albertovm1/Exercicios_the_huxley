while True:
    n_inicial = int (input())
    if n_inicial>=1:
        break
    print("Insira um número inicial entre 1 e 9")
while True:
    n_final = int (input())
    if n_inicial<1 or n_final>9 or n_final<1:
        print("Insira um número final entre 1 e 9")
    elif n_inicial>n_final:
        print("Nenhuma tabuada nesse intervalo")
        break
    elif n_final<=9:
        for i in range (n_inicial, n_final+1):
            if n_inicial>0 and n_final<=9:
                for j in range(1, 10):
                    print(f"{i} x {j} = {i*j}")
                print()
        break