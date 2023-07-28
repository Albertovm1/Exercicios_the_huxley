a = int(input())
if a >= 1:
        print("1", end=" ")
for i in range(1, a+1):
    for j in range(2, i):
        if (i % j) == 0:
            print (i, end=" ")
            break