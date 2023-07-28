while True:
    n = int(input())
    if n == 0:
        break
    num1 = 0
    num2 = 1
    string = ""
    for a in range(0, n):
        if a != n-1:
            string += str(num1) + " "
        else:
            string += str(num1)
        num3 = num1 + num2
        num1 = num2
        num2 = num3
    print(string)