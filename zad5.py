
bokA=int(input("podaj bok a: "))
bokB=int(input("podaj bok b: "))
bokC=int(input("podaj bok c: "))
if  bokA> bokB+bokC:
    print("mozna zbudowac trojkat")
elif bokB> bokC+ bokA:
    print("mozna znudowac trojkat")
elif bokC> bokB+bokA:
    print("mozna zbudowac trojkat")
else :
    print("niemozna zbudowac trojkata")