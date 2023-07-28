# Bezaliel sempre ataca, clodes aumenta o dano
from math import ceil

n = int(input())
for i in range(n):
    vc, vb, dc, db = map(int, input().split())

    turnos_v_b = ceil(vc/db) # Turnos para vitória de Clodes
    turnos_v_c = ceil(vb/dc) # Turnos para vitória de Bezaliel

    while vc > 0 and vb > 0:
        if turnos_v_c > turnos_v_b:
            dc += 50
        else:
            vb -= dc
        turnos_v_c = ceil(vb / dc)
        vc -= db
        turnos_v_b = ceil(vc/db)

    if vb <= 0:
        print("Clodes")
    else:
        print("Bezaliel")