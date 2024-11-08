import random

conjunto_1 = set()
conjunto_2= set()

cont = 0
while cont<=10:
    aleatorio_1 = random.randint(1, 15)
    aleatorio_2 = random.randint(1, 15)
    conjunto_1.add(aleatorio_1)
    conjunto_2.add(aleatorio_2)
    cont+=1

union = conjunto_1 | conjunto_2

print(f"Conjunto 1: {conjunto_1}")
print(f"Conjunto 2: {conjunto_2}")
print(union)

rep = 0
for i in conjunto_1:
    for y in conjunto_2:
        if i==y:
            rep+=1

print(rep)        
