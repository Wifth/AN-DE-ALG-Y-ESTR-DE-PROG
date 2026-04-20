#haz el codigo de busqueda binaria segun lo visto en clase

lista = [4,5,10,15,20,25,30,35,40,45,50,58,65,80,98]
num = int(input("Ingrese numero a buscar:\n"))


lower = 0
higher = len(lista)
while lower + 1 < higher:
    middle = (lower + higher)//2
    if lista[middle] == num:
        break
    elif lista[middle] > num:
        higher = middle
    elif lista[middle] < num:
        lower = middle

if lista[middle] == num:
    print(f"Encontrado en la posicion {middle+1}")
else:
    print("NO Encontrado")

