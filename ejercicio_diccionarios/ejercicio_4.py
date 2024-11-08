
diccionario = dict()
for i in range(1, 6, 1):
        b = i*i
        c = b
        b = c
        diccionario[i]=b

print(f"Con for: {diccionario}")    

###################################

diccionario_2 = {x:x*x for x in range(1, 6, 1)}
print(f"con for_2: diccionario_2")