codigoInt = int(input("Codigo ->"))
nombreStr = input("Nombre -> ")
existenciasInt = 0
controlBln = True
import os 
while controlBln == True:
    os.system("cls")
    print("Codigo: ", codigoInt, '\nNombre: ', nombreStr, '\nExistencias: ', existenciasInt)
    opcionStr = input("1. compras\n2. Ventas\n3. Reportes\n -> ")
    cantidadInt = int(input("Cantidad: "))
    if opcionStr == "1":
        existenciasInt += cantidadInt
    if opcionStr == "2":
        if existenciasInt <= cantidadInt:
            existenciasInt -= cantidadInt
        else: 
            print("\nNo hay suficientes existencias")
    if opcionStr == "3":
        print("cantidad actual de inventario: ", existenciasInt)
    if opcionStr == "4":
        controlBln = False

                      
