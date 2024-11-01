id_estudiantes = {112, 113, 115, 116, 117}
print(id_estudiantes)

#conjuntos mixtos
mixto = {'hello', 1001, -2, 'bye'}
print(mixto)

#creacon de conjunto con el constructor set()
conjunto_vacio = set()
print(conjunto_vacio)

#union
conjunto_1 = {1, 2, 3, 4}
conjunto_2 = {5, 6, 7, 8}

union = conjunto_1 | conjunto_2
print(union)

#interseccion
interseccion = conjunto_1 & conjunto_2
print(interseccion)

#diferencia
diferencia = conjunto_1 - conjunto_2
print(diferencia)

#diferencia simetrica
diferencia_simetrica = conjunto_1 ^ conjunto_2
print(diferencia_simetrica)

#Agregar un elemento a un conjunto
id_estudiantes.add(580)
print(f"Agrego ultimo elemento {id_estudiantes}")

#eloiminar un alemento de un conjunto
id_estudiantes.remove(580)
print(f"Elimino ultimo elemento {id_estudiantes}")

#verificar si esta presente un elemento
presente = 115 in id_estudiantes
print(f"Esta presente {presente}")

#para limpiar un elemento
conjunto_3 = {1, 2, 3, 4, 5, 6}
print(f"Limpio elemento {conjunto_3}")

#iterar sobre un conjunto
for elemento in id_estudiantes:
    print(elemento)

#eliminar elementos duplicados de una lista
lista = [1, 2, 3, 4, 5, 5, 4]
conjunto = set(lista)
lista = list(conjunto)
print(lista)

#eliminar elementos duplicados de una tupla
tupla = (1, 2, 3, 4, 5, 5, 4)
conjunto = set(tupla)
tupla = tuple(conjunto)
print(tupla)

#eliminar elementos duplicados de una cadena
cadena = 'Hola mundo'
conjunto = set(cadena)
cadena = ''.join(conjunto)
print(cadena)

