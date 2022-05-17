a=int(input("Podaj a: "))

b=int(input("Podaj b: "))

licznik = 0

if b==0:
    print("NWD wynosi:", a)
else:


     while b>0:
         licznik += 1
         reszta=a%b
         a=b
         b=reszta
    
print("NWD wynosi: ", a )