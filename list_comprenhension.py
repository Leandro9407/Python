animales = ["gata", "perro", "leon", "elefante", "conejo"]

lista_nueva = [animal for animal in animales if "a" in animal]
print(lista_nueva)

####################################################

l_1 = ["Perez", "Ramirez", "Osorio"]
l_2 = ["Ana", "Juan", "Sonia"]

l_3 = [l_2[i] + ":" + l_1[i] for i in range(0, len(l_1))]
print(l_3)

#####################################################

animales_2 = [[animal, animal.count("a")] for animal in animales if "a" in animal]
print(animales_2)

############################################################
#para generar un diccionario

lenguajes = ["Python", "Java", "Python", "JavaScript", "Php"]
d = {lenguaje: lenguajes.count(lenguaje) for lenguaje in lenguajes}
print(d)