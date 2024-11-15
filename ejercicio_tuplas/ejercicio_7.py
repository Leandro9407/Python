tupla_calificaciones = ((10, 10, 10, 12), (30, 45, 56, 45), (81, 80, 39, 32), (1, 2, 3, 4))

conver = list(tupla_calificaciones)

lista_calificaciones = []
for c in conver:
    lista_calificaciones.append(list(c))



lista_promedio = []
incre = 0

for i in lista_calificaciones:
    suma = 0
    cont = 0
    for c in range(len(i)):    
        suma += lista_calificaciones[c][incre]
        cont+=1
        if cont==4:
            suma = suma / 4
            lista_promedio.append(suma)
            incre+=1


print(lista_promedio)

print("")


####################################################

lista_promedio_2 = []
for col in range(len(lista_calificaciones[0])):  # Asume que todas las sub-listas tienen la misma longitud
    suma = 0
    for fila in lista_calificaciones:
        suma += fila[col]
    promedio = suma / len(lista_calificaciones)
    lista_promedio_2.append(promedio)

print(lista_promedio_2)

        
      