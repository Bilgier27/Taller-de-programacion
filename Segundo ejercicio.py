import os
os.system('cls')

totalF = 0
productos_seleccionados = []

capturar_cantidad = 0
cons_computador = 1500000
cons_computadordeescritorio = 2800000
cons_tabletas = 700000
cons_videobeam = 1200000
cons_televisor = 1700000
facturar = True
while facturar:
    os.system('cls')
    print("<<<< MENU DE OPCIONES >>>>\n\n1. Computador ->\n2. Computador de escritorio ->\n3. Tabletas ->\n4. Videobeam ->\n5. Televisor ->\n0. Facturar\n ->")

    opcion = int(input("Ingrese una opcion: "))

    if opcion == 0:
        facturar = False
        break

    cantidad = int(input("Cantidad: "))

    if opcion == 1:
        print("Computador")
        totalF += (cantidad * cons_computador)
        print(f"\nTotal: {totalF}$")
        productos_seleccionados.append(f"{cantidad} Computador")
    
    elif opcion == 2:
        print("Computador de escritorio")
        totalF += (cantidad * cons_computadordeescritorio)
        print(f"\nTotal: {totalF}$")
        productos_seleccionados.append(f"{cantidad} computadordeescritorio")
        
    elif opcion == 3:
        print("Tabletas")
        totalF += (cantidad * cons_tabletas)
        print(f"\nTotal: {totalF}$")
        productos_seleccionados.append(f"{cantidad} tabletas")
        
    elif opcion == 4:
        print("Videobeam")
        totalF += (cantidad * cons_videobeam)
        print(f"\nTotal: {totalF}$") 
        productos_seleccionados.append(f"{cantidad} videobeam")
        
    elif opcion == 5:
        print("Televisor")
        totalF += (cantidad * cons_televisor)
        print(f"\nTotal: {totalF}$")
        productos_seleccionados.append(f"{cantidad} televisor")

    input('enter para continuar')

print("\nCANTIDADES SELECCIONADAS:", ", ".join(productos_seleccionados))
print(f"\nTOTAL A PAGAR......................", totalF)




    




        



