
lista = [5, 4, 16, 5, 75, 8, 5, 45, 1, 12, 3, 21, 4, 14, 6, 8, 36, 67, 77, 9]

lista.sort()

print(f"Usando Sort:")
print(lista[-1])
print(lista[0]) 

print(f"")
######## Usando FOR ##########
print(f"#"*64)

lista_2 = [5, 4, 16, 5, 75, 8, 5, 45, 1, 12, 3, 21, 4, 14, 6, 8, 36, 67, 77, 9]

mayor = 0
menor = 100

print(f"")
print(f"Usando For:")

for num in lista_2:
    if num>=mayor:
        mayor=num

print(mayor)

for men in lista_2:
    if men<=menor:
        menor=men

print(menor)
