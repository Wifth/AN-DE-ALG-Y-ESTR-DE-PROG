def suma(number_1, number_2):
    return number_1 + number_2

def suma2(n1 : int, n2: int) -> int:
    return n1 + n2

def suma3(n1 : int = 0, n2: int = 3) -> int:
    return n1 + n2

print (suma(2,3))
print (suma2(2,3))
print (suma3(2))

def spam():
    global eggs
    eggs = "spam"

eggs = "global"
spam()
print(eggs)