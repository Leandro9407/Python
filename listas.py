#lista vacia
lista_1 = []

#lista mixta
lista_2 = [1, 2, 3, 4, "azul", "gato", "perro"]

print(f"Lista_2: {lista_2[4]}") #para acceder a una posicion de la lista
print(f"Lista_2: {len(lista_2)}") #para saber cual es la longitud de la lista
print(f"Lista_2[-2]: {lista_2[-2]}") #para recorrer el arreglo hacia atras


#lista anidadas
lista_3 = [8, 14, lista_2, "lobo", 70]
print(f"Lista_3: {lista_3}")
lista_10 = lista_3[2][4]    #para buscar una posicion dentro de otra lista
print(f"Lista_10: {lista_10}")

#slicing especificar las posiciones de la lista
print(f"Lista_2: {lista_2[2:5]}") #de:hasta
print(f"Lista_2: {lista_2[2:]}") #de:hasta el final

print(f"lista: {lista_3[2][4]}") #para acceder a la lista dentro de un lista en una posicion especifica

#modificar el valor de un elemento en determinado indice
lista_3[0]=10
print(f"Lista_3: {lista_3}")


#for item in lista: para iterar toda la lista
for item in lista_2:
    print(item)

################## MÉTODOS DE LISTAS #################      
lista_nueva = [9, 8, 7, 6, 5,]

#APPEND permite añadir elementos al final de una lista
lista_nueva.append('cuatro')
print(lista_nueva)

lista_nueva.append(lista_2) #para agregar una lista a la lista
print(lista_nueva)

#CLEAR deja la lista vacia
lista_nueva.clear()
print(lista_nueva)

#COPY sirve para desenlazar la lista
lista_4=lista_3.copy() #desenlazo la lista_3 de la lista_4
lista_4[0]=22
print(f"Lista_4: {lista_4}")

#COUNT cuenta el numero de veces que aparece un numero en la lista
conteo = lista_2.count(2)
print(conteo)

#EXTEND sirve para concatenar listas de forma elegante
lista_2.extend(lista_3)
print(lista_2)

#INSERT insertar un elemento en un indice especifico
nombres = ['octavio', 'Lucrencio', 'Alfaro', 'Guzman']
nombres.insert(2, "Leandro")
print(nombres)

#REMOVE sirve para remover un elemento en un indice especificado
nombres.remove('Guzman')
print(nombres)

#POP sirve para remover el ultimo elemento de la lista
nombres.pop()
#nombres.pop(2) para remover el elemento del indice de la lista
print(nombres)

#REVERSE invertir la lista
nombres.reverse()
print(nombres)

#SORT ordena la lista en un orden requerido, tambien funciona con string (ordena en orden alfabetico)
numero = [9, 6, 3, 5, 1, 4]

numero.sort() # de menor a mayor
print(numero)

numero.sort(reverse=True) # para ordenar la lista de mayor a menor
print(numero)


#desempaquetamiento
lista_5 = [10, "hola", 30]

a, b, c = lista_5   #cada valor de la fila se emparenta con cada variable a, b, c
print(f"a={a}, b={b}, c={c}")


#desempaquetamiento con comodines
lista_6 = [10, "hola", 30, 40, 50, 60]

a, b, c, *resto = lista_6  
print(f"a={a}, b={b}, c={c}, d={resto}")

