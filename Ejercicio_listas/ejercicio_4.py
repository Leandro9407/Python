lista = [5, 8, 5, 9, 5, 7, 6, 5, 5, 2, 1, 5, 6, 5, 7]
print(f"Lista original: {lista}")

for i in lista:
    if i==5:
        lista.remove(5)


print(f"Lista modificada: {lista} \n")      


############## SET ##############
print("#"*64)

lista_2 = [8, 6, 8, 5, 1, 5, 7, 8, 3, 4, 6, 7, 2]
print(f"Lista original: {lista_2}")

nueva_lista = set(lista_2)
print(f"Lista modificada con SET: {nueva_lista} \n") 


############# NOT IN ###############
print("#"*64)
lista_3 = [5, 8, 2, 9, 5, 7, 6, 5, 8, 2, 1, 5, 6, 5, 7]
print(f"Lista original: {lista_3}")

nueva_lista_2 = []
for i in lista_3:
    if i not in nueva_lista_2:
        nueva_lista_2.append(i)

print(f"Lista modificada con NOT IN: {nueva_lista_2}")    


