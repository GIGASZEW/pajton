import random
a= input("Wpisz: Papier, Kamien, Nozyce")
b= ["Papier","Kamien","Nozyce"]
c=random.choice(b)
print(f"Twoj wybor {a} , wybor  {c}     ")

if a==c:
    
    print(f"Oboje gracze wygrali {a}, Jest remis")

elif a=="Kamien":
    if c=="Nozyce":
        print("Kamien niszczy nozyczki! Wygrywa")
    else:
        print("Papier zakrywa kamien.!Przegrywasz NOBIE")
elif a=="Papier":
    if c=="Kamien":
        print("Papier zakrywa kamien! Wygrywasz")
    else:
        print("nozyczki przecinaja papier. Przegrywasz NOBIE")
elif a=="Nozyce":
    if c=="Papier":
        print("nozyce przecinaja papier! WYGRYWASZ")
    else:
        print("kamien rozwala nozyczki! PRZEGRYWASZ NOBIE")







