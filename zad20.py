x=int(input("Ile liczb trzeba wypisac?"))
def genFib(n):
    a=0
    b=1
    for i in range(n+1):
       yield a
       a, b = b, a + b
        
print(list(genFib(x)))