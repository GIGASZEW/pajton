from logging import shutdown
from tracemalloc import stop
from click import pause

import sys
a=int(input("podaj a"))
h=int(input("podaj h"))

while a<=0 or h<=0:
    print("niema takiej figury sprobuj uruchomic program ponownie i podaj dobre dane lub dobrze zczytaj dane!!!!!!!!!!!!!!!!!! ")
    sys.exit(0)
   

typ=int(input("pole szescianu=1, Pole Ostroslupa prawidlowego czworokatnego=2"))

    
if typ==1:
    objetosc1=a*a*a
    print("objetosc szescianiu wynosi:", objetosc1 )
elif typ==2:
    objetosc2=1/3*(a*a)*h
    print("objetosc ostroslupa wynosi:", objetosc2)