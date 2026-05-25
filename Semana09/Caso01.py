## Ejercicio2: Crear una función recursiva que permita multiplicar 2
## números enteros

##Función mult
def mult(num1, num2):
    if num2 == 0:
        return 0
    if num2 > 0:
        return num1 + mult(num1, num2 - 1)
    return -mult(num1, -num2)

## Bloque principal
numero1 = 5
numero2 = -8
resultado = mult(numero1, numero2)
print(f"El producto de {numero1} y {numero2} es {resultado}")