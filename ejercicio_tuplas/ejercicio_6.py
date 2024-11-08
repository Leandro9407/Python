lista = [(), (), (","), ("a", "b"), ("a", "b", "c"), ("d")]
print(f"Lista original: {lista}")

while () in lista:
    lista.remove(())

print(f"Lista modificada con while: {lista}")
print("")

##############################################

lista_nueva = []
for i in lista:
    if i!=():
        lista_nueva.append(i)

print(f"Lista modificada con for: {lista_nueva}")        
