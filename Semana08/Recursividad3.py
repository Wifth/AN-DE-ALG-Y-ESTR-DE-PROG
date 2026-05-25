"""
Pida un valor y usando recursion 
muestre todos los valores entre 1 
y ese que son multiplos de 3 
"""
def recx(x,n): 
    if x > n: 
        return 
    else: 
        if x % 3 == 0: 
            print (x) 
        recx(x+1,n) 
            
n = int(input("Ingrese un número: ")) 
recx(1,n)