num = int (input())
num2 = int (input())
if num > num2:
  limite_inferior = num2
  limite_superior = num
else:
  limite_inferior = num
  limite_superior = num2
soma = 0
for i in range(limite_inferior, limite_superior + 1):
    if i > 0:
        soma += i
print(soma)