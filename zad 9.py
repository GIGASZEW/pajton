a=float(input("podaj waga"))
b=float(input("podaj wzrost w metrach"))
bmi=a/b**2
if bmi<=20:
    print("niedowaga",bmi)
elif 25>=bmi>=20:
    print("prawidlowa waga",bmi)
elif 25>=bmi<30:
    print("Nadwaga ", bmi)
else:
    print("Otyłosc", bmi)
