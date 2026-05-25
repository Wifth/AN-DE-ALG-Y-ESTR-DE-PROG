def torres_de_hanoi (n, origen, destino, auxiliar):
    if n == 1:
        print(f"Mover disco 1 de varilla {origen} a varilla {destino}.")
        return
    
    # Paso 1: Mover n-1 discos al auxiliar.
    torres_de_hanoi(n-1, origen, auxiliar, destino)

    # Paso 2: mover el disco grande al destino.
    print(f"Mover disco {n} de varilla {origen} a varilla {destino}.")

    # Paso 3: Mover los n-1 discos del auxiliar al destino.
    torres_de_hanoi(n-1, auxiliar, destino, origen)

# Ejemplo de uso para 3 discos
print("Movimientos para 3 discos: ")
torres_de_hanoi(4, 'A', 'C', 'B')