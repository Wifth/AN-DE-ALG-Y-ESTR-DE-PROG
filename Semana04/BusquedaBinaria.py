#haz el codigo de busqueda binaria segun lo visto en clase
def busqbin(lst, num):
    lower = 0
    higher = len(lst)
    while lower + 1 < higher:
        middle = (lower + higher)//2
        if lst[middle] == num:
            return True
        elif lst[middle] > num:
            higher = middle
        elif lst[middle] < num:
            lower = middle
    return False

lista = [4,5,10,15,20,25,30,35,40,45,50,58,65,80,98]
n = int(input("Ingrese numero a buscar:\n"))
if busqbin(lista, n):
    print("Encontrado")
else:
    print("NO Encontrado")