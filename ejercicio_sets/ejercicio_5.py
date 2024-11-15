import random

conjunto = set()

cont = 0
while cont<=10:
    aleatorio = random.randint(1, 15)
    conjunto.add(aleatorio)
    cont+=1


lista = list(conjunto)
random.shuffle(lista)
print(f"Números: {lista}")
mayor = 0
num_1 = 0
num_2 = 0
for i in lista:
    for y in range(i + 1):
        producto = i*y
        if producto>=mayor and i!=y:
            mayor=producto
            num_1= i
            num_2 = y

print(f"Número mayor: {mayor}")
print(f"Pares: {num_1} y {num_2}")            