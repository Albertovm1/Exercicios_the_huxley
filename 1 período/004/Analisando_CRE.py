menor_cre = float("inf")
matricula_menor_cre = None
soma_cre = 0
quantidade_alunos = 0

while True:
    matricula = input()
    if matricula == "999":
        break
    cre = float(input())
    quantidade_alunos += 1
    soma_cre += cre
    if cre < menor_cre:
        menor_cre = cre
        matricula_menor_cre = matricula

media_cre = soma_cre / quantidade_alunos
print(matricula_menor_cre)
print(f"{media_cre:.2f}")
