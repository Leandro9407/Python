
tuplas = (10, 5, 6, 9, 45, 63, 8, 7)

desempaquetar = [*tuplas]
suma = 0
for i in desempaquetar:
    suma = i + suma

print("Usando el desempaquetamiento de tupla a lista")
print(f"La suma de la tupla es: {suma}")  
print("") 

#########################################

a, b, *dos = tuplas
suma_2 = 0 + a + b
for y in dos:
    suma_2 = y + suma_2

print("Usando desempaquetamiento con comodin")
print(f"La suma es: {suma_2}")    
print("")

#######################################

tres = tuplas
suma_3 = 0
for u in tres:
    suma_3 = u + suma_3

print("Usando desempaquetamiento normal")
print(f"La suma es: {suma_3}")    