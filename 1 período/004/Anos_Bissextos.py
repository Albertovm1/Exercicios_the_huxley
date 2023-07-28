anoi, anof = map(int, input().split())
ano_b = 0
for ano in range(anoi, anof+1, 1):
    if ano % 4 == 0 and (ano % 100 != 0 or ano % 400 == 0):
        print(ano)
        ano_b += 1
if ano_b == 0:
    print("-1")