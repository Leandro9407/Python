#lista vacia
lista_1 = []

#lista mixta
lista_2 = [1, 2, 3, 4, "azul", "gato", "perro"]

print(f"Lista_2: {lista_2[4]}")
print(f"Lista_2: {len(lista_2)}") #para saber cual es la longitud de la lista
print(f"Lista_2[-2]: {lista_2[-2]}") #para recorrer el arreglo hacia atras


#lista anidada
lista_3 = [8, 14, lista_2, "lobo", 70]
print(f"Lista_3: {lista_3}")

#slicing especificar las posiciones del array
print(f"Lista_2: {lista_2[2:5]}")
print(f"Lista_2: {lista_2[2:]}")

print(f"lista: {lista_3[2][4]}") #para acceder a la lista dentro de un lista en una posicion especifica