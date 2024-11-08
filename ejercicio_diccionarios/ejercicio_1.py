keys = ["Ten", "Twenty", "Thirty"]
values = [10, 20, 30]

diccionario = dict()

for i in range(3):
    diccionario[keys[i]]=values[i]

print(f"Creando diccionario con for: {diccionario}") 
            
###################################################

diccionario_2 = dict(zip(keys, values))
print(f"Creando diccionario con zip: {diccionario_2}")
