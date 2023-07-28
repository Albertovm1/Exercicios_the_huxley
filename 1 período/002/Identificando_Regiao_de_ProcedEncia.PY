Codigo_de_origem=int(input())

if Codigo_de_origem==1:
    print("Nordeste")
if Codigo_de_origem==2:
    print("Norte")
if (Codigo_de_origem==3 or Codigo_de_origem==4):
    print("Centro-Oeste")
if Codigo_de_origem>4 and Codigo_de_origem<=9:
    print("Sul")
if Codigo_de_origem>9 and Codigo_de_origem<=15:
    print("Sudeste")