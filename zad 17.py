import random

slowa=("pies","ok","pies")

zycia =3
zgadywanie=random.choice(slowa)
dlugosc=len(zgadywanie)
tablica=["_"]*dlugosc
while zycia>0:
    print(*tablica)
    litera=input("Podaj Literę:  ")
    if litera in zgadywanie:
        print("jest")
        for i in range (dlugosc):
            if zgadywanie[i]==litera:
                tablica[i]=litera
    else:
        print("niema!") 
        zycia=-1
    if "_" not in tablica:
        print("WYGRANA")
        exit()
    elif zycia==0:
        print("Przegranyyyyyyyyyyyyyy")   
        exit()