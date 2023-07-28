def convesor_horas(horas, minutos):
    if horas == -1:
        return
    elif horas == 12:
        periodo = "P.M"
    elif horas == 0:
        horas = 12
        periodo = "A.M"
    elif horas == 24:
        horas = 0
        periodo = "A.M"
    elif horas < 12: 
        periodo = "A.M"
    else:
        horas = horas - 12
        periodo = "P.M"
    return f"{horas}:{minutos} {periodo}"
while True:
    horas, minutos = map(int, input().split(":"))
    horas_convertida = convesor_horas(horas, minutos)
    if horas == -1:
        break
    print(horas_convertida)