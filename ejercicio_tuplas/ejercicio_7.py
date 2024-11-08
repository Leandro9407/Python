tupla_calificaciones = ((10, 10, 10, 12), (30, 45, 56, 45), (81, 80, 39, 32), (1, 2, 3, 4))

conver = list(tupla_calificaciones)

lista_calificaciones = []
for c in conver:
    lista_calificaciones.append(list(c))

cont = 0
suma = 0
lista_promedio = []

for i in lista_calificaciones:
    for c in range(len(i)):    
        suma += lista_calificaciones[c][0]
        cont+=1
        if cont==4:
            suma = suma / 4
            lista_promedio.append(suma)
            cont = 0
            suma = 0


print(lista_promedio)

        
      