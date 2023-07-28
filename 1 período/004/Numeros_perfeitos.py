n = int(input())
num = 1
while num < n:
    soma_divisores = 0
    for i in range(1, num):
        if num % i == 0:
            soma_divisores += i
    if soma_divisores == num:
        print(num)
    num += 1