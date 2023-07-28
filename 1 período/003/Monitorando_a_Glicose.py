soma_taxa = 0
quantidade_d_taxa = 0

while True:
    taxa = int(input())
    if taxa == 0:
        break
    soma_taxa+=taxa
    quantidade_d_taxa += 1 
media = soma_taxa/quantidade_d_taxa
if media <= 110:
    print("Glicose Normal")
elif media >= 200:
    print("Glicose Muito Alta")
else:
    print("Glicose Alterada")