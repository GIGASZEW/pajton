print("nie podawaj 0")
a=int(input("podaj a"))
b=int(input("podaj b"))
typ=int(input ("mnozenie-1 odejmowanie-2 dodawanie-3 dzielenie-4"))
c=a*b
d= a-b
e= a+b
f= a/b
if typ==1:
    print ("mnozenienie=:", c)

elif typ==2:
    print ("odejmowanie=", d)

elif typ==3:
    print ("dodawanie=", e)
elif typ==4 :
    
    print("Dzielenie wynosi=", f)