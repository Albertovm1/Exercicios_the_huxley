def verificar_vencedor(tabuleiro):
    for linha in tabuleiro:
        if linha[0] == linha[1] == linha[2] and linha[0] != '_':
            return linha[0]
    for coluna in range(3):
        if tabuleiro[0][coluna] == tabuleiro[1][coluna] == tabuleiro[2][coluna] and tabuleiro[0][coluna] != '_':
            return tabuleiro[0][coluna]
    if tabuleiro[0][0] == tabuleiro[1][1] == tabuleiro[2][2] and tabuleiro[0][0] != '_':
        return tabuleiro[0][0]
    if tabuleiro[0][2] == tabuleiro[1][1] == tabuleiro[2][0] and tabuleiro[0][2] != '_':
        return tabuleiro[0][2]
    return

def estado_jogo(tabuleiro):
    vencedor = verificar_vencedor(tabuleiro)
    if vencedor:
        print(vencedor)
    elif '_' in [elemento for linha in tabuleiro for elemento in linha]:
        print("Empate ou em andamento")

while True:
    tabuleiro = []
    for _ in range(3):
        linha = input().split()
        tabuleiro.append(linha)
    if tabuleiro == "sair":
        print("erro")
        break
    estado_jogo(tabuleiro)
    print()