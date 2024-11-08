tupla = ((1, 20), (3, 40), (20, 50), (9, 12), (90, 12))
print(f"Tupla original: {tupla}")

ordenar = tuple(sorted(tupla))
print(f"Tupla de tuplas ordenada con SORTED: {ordenar}")

##################################################

lista = list(tupla)
lista.sort()
tuplas = tuple(lista)
print(f"Tupla de tuplas ordenada con SORT: {tuplas}")

