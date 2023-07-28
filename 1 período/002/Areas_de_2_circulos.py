raio_01=float(input())
raio_02=float(input())

a_01=3.14*raio_01**2
a_02=a=3.14*raio_02**2

if a_01 > a_02:
    print ("Primeiro círculo")

if a_01 < a_02:
    print ("Segundo círculo")

if a_01 == a_02:
    print ("Iguais")