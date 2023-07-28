RAIO= float(input())
ANGULO=float(input())

C=ANGULO*3.14*RAIO/180
A=3.14*RAIO**2*ANGULO/360

print("{:.2f}".format(C))
print("{:.2f}".format(A))