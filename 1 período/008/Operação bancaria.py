def ler_operacoes():
    operacoes = []
    while True:
        entrada = input().split()
        operacao = int(entrada[0])
        entrada[0]
        if operacao == -1:
            break
        valor = float(entrada[1])
        operacoes.append([operacao, valor])
    return operacoes

def executar_operacoes(operacoes):
    saldo = 0.0
    total_creditos = 0.0
    total_debitos = 0.0
    for operacao in operacoes:
        if operacao[0] == 1:
            saldo += operacao[1]
            total_creditos += operacao[1]
        elif operacao[0] == 0:
            saldo -= operacao[1]
            total_debitos += operacao[1]
    return saldo, total_creditos, total_debitos

def imprimir_resumo(total_creditos, total_debitos, saldo):
    print(f"Creditos: R$ {total_creditos:.2f}")
    print(f"Debitos: R$ {total_debitos:.2f}")
    print(f"Saldo: R$ {saldo:.2f}")

operacoes = ler_operacoes()
saldo, total_creditos, total_debitos = executar_operacoes(operacoes)
imprimir_resumo(total_creditos, total_debitos, saldo)