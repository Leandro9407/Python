#tuplas
tupla = (4, 5, 9)
print(tupla)

#len para saber la longitud de la tupla
longitud = len(tupla)

#convertir lista a tupla o viceversa
tupla_2 = (4, 5, 9)
lista_t = tuple(tupla_2) 
print(f"Convertido a: {tupla_2}")

#desempaquetamiento
lista_5 = (10, "hola", 30)

a, b, c = lista_5   #cada valor de la fila se emparenta con cada variable a, b, c
print(f"a={a}, b={b}, c={c}")


#desempaquetamiento con comodines
lista_6 = (10, "hola", 30, 40, 50, 60)

a, b, c, *resto = lista_6  #a=10, b="hola", c=30, resto=40, 50, 60
print(f"a={a}, b={b}, c={c}, d={resto}")


#desempaquetar de tupla a lista
mi_tupla = (1, 2, 3, 4, 5)
mi_lista = [*mi_tupla]
print(mi_lista)

#buscar un elemento en una tupla
if "hola" in lista_6:
    print(f"Encontrado")

#iterar una tupla
for i in mi_tupla:
    print(i)    


#ejemplo modificar una tupla
frutas = ("manzana", "banano", "cereza")
lista_f = list(frutas)
lista_f[1] = "peras"

frutas = tuple(lista_f)

print(frutas)

#count cuentas la veces que aparece un elemento
cars = ('Ford', 'BMW', 'Volvo')
buscar_1 = cars.count('Ford')
print(buscar_1)

#index muestra el indice
buscar_2 = cars.index('Ford')
print(buscar_2)


#crear tupla de un elemento
thistuple = ("apple",)
print(type(thistuple))

#no tupla
thistuple = ("apple")
print(type(thistuple))
