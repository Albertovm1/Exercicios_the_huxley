n = int (input())
p = int (input())
contador = 0
for i in range (n):
    x = int (input())
    y = int (input())
    r = x + y
    if (r >= p) and (x != 0 and y != 0):
        contador += 1
print(contador)