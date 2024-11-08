tupla = (1, 2, 3, 4)
print(f"Tupla original: {tupla}")

lista = list(tupla)
lista.append(5)
tupla = tuple(lista)

print(f"Tupla con un elemento añadido: {tupla}")
