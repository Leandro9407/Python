id_estudiantes = {112, 113, 115, 116, 117}
print(id_estudiantes)

#conjuntos mixtos
mixto = 'hello', 1001, -2, 'bye'
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