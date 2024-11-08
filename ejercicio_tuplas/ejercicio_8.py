colores = (('Red', 'White', 'Blue'), ('Green', 'Pink', 'Purple'), ('Orange', 'Yellow', 'Lime'))

buscar = input("Ingrese color a encontrar: ")

no_encontrado = 0
encontrado = False
for b in colores:
    for c in b:
        if buscar==c:
            encontrado = True
            print(f"Elemento encontrado: {encontrado}")
            print(f"Posición: {b.index(buscar)}")
            print(f"Indice: {colores.index(b)}")
            no_encontrado+=1


if no_encontrado==0:
    print(f"Elemento encontrado: {encontrado}")   
    print("Sin posición")  
        