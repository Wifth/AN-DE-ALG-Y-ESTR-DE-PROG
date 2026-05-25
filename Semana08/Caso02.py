def recx(x, n): 
    if x == n: 
        if x % 3 == 0: 
            print(x) 
            return 
    else: 
        if x % 3 == 0: 
            print(x) 
        recx(x + 1, n) 

num = int(input("Ingrese un número: ")) 
recx(1, num)

"""
def multiplos(numActual, numFinal): 
    if numActual > numFinal: 
        return 
    if numActual % 3 == 0: 
        print(numActual) 
    multiplos(numActual + 1, numFinal) 

limite = int(input("Ingrese un valor limite: ")) 
print(f"\nLos multiplos de 3 son los siguientess:") 
multiplos(1, limite)
"""