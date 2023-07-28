def eh_primo(x):
    for i in range(2, x):
        if x % i == 0:
            return False
    return True

def marsenne(x):
    if eh_primo(x) and eh_primo(2 ** x - 1):
        return True

while True:
    m = int(input())
    if m < 0:
        break
    for i in range(1, m):
        if marsenne(i):
            print(i, end=" ")
    print()