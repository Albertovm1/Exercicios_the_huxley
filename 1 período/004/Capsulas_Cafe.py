total_capsulas = 0
for i in range(7):
    quantidade_caixas = int (input())
    tamanho_caixas = input()
    if tamanho_caixas == "P" or tamanho_caixas == "p":
        total_capsulas += 10 * quantidade_caixas
    elif tamanho_caixas == "G" or tamanho_caixas == "g":
        total_capsulas += 16 * quantidade_caixas
print(total_capsulas)
print((total_capsulas//7)*2)