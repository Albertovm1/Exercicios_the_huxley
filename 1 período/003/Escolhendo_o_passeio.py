bol = 0
cin = 0
for a in range(7):
    passeio = input()
    if passeio.lower() == "cinema":
        cin += 1
    else:
        bol += 1

if bol > cin:
    print("BOLICHE")
else:
    print("CINEMA")