NOTA_O1=float(input())
NOTA_02=float(input())
NOTA_03=float(input())

PESO_01=float(input())
PESO_02=float(input())
PESO_03=float(input())

M_A=(NOTA_O1+NOTA_02+NOTA_03)/3
M_P=(NOTA_O1*PESO_01+NOTA_02*PESO_02+NOTA_03*PESO_03)/(PESO_01+PESO_02+PESO_03)
M_H=3/((1/NOTA_O1)+(1/NOTA_02)+(1/NOTA_03))

print("a: ""{:.1f}".format(M_A))
print("p: ""{:.1f}".format(M_P))
print("h: ""{:.1f}".format(M_H))