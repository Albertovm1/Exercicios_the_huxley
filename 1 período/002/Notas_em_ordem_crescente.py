nota_01 = int(input())
nota_02 = int(input())
nota_03 = int(input())

if(nota_01 > nota_02):
        aux = nota_01
        nota_01 = nota_02
        nota_02 = aux

if(nota_01 > nota_02):
        aux = nota_01
        nota_01 = nota_02
        nota_01 = aux

if(nota_02 > nota_03):
        aux = nota_02
        nota_02 = nota_03
        nota_03 = aux

print(nota_01)
print(nota_02)
print(nota_03)