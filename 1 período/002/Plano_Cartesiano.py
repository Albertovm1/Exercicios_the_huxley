X=int(input())
Y=int(input())

if X>0 and Y>0:
    print("Primeiro Quadrante")
if X<0 and Y>0:
    print("Segundo Quadrante")
if X<0 and Y<0:
    print("Terceiro Quadrante")
if X>0 and Y<0:
    print("Quarto Quadrante")
if X==0 and Y==0:
    print("Sobre a origem")
if X==0 and (Y>0 or Y<0):
    print("Sobre o eixo y")
if Y==0 and (X>0 or X<0):
    print("Sobre o eixo x")