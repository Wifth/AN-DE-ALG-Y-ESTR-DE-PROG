"""
Dado un arreglo de enteros, diseñar e 
implementar algoritmos recursivos que 
calculen El mayor elemento de un arreglo
"""

def mayorLista(lst):
    ult = len(lst)-1
    return mayorL(lst, ult, lst[ult])
    

def mayorL(lst, pos, mayor):
    if pos == 0:
        return mayor if mayor > lst[pos] else lst[pos]
    else:
        m = mayor if mayor > lst[pos] else lst[pos]
        return mayorL(lst, pos - 1, m)

lista = [3,8,5,9,7]

print(mayorLista(lista))