diccionario_1 = {'Pedro':10, 'Oscar':30, "Arturo":40}
diccionario_2 = {"Ivan":20, "Pepe":50, "Alejandro":60}

concatenacion_1 = diccionario_1 | diccionario_2
print(f"Concatenación con |: {concatenacion_1}")

#################################################
diccionario_1.update(diccionario_2)
print(f"Concatenación con update: {diccionario_1}")

################################################
concatenacion_3 = {**diccionario_1, **diccionario_2}
print(f"Concatenación con desempaquetamiento: {concatenacion_3}")

