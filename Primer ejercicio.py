#Crear algoritmo que me permita poner numeros entre 10 y 20 hasta que desee salir.
numeros = int(input('Ingrese la cantidad de numeros que desea evaluar: '))
contador = 0
i = 0
while i < numeros:
    num1 = float(input(f"Ingrese el numero {i + 1}: "))
    if num1 >= 10 and num1 <= 20:
        contador += 1
    i += 1

print(f'La cantidad de numeros en el rango de 10 a 20 es: {contador}')
