import random

print("GENERADOR DE CONTRASEÑA")

letras = ("a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "ñ", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z")

caracteres = ("!", "+", "-", "_", "*", "/", "?", "=", "#", "$", "%", "&", "¡", "¿")

############## mayusculas ####################
generar_mayusculas = input("Ingrese cantidad de letras mayúsculas: ")
mayusculas = int(generar_mayusculas)

cadena_mayusculas = []
n_veces_uno = 1    
while n_veces_uno<=mayusculas:
    numero_aleatorio_1 = random.randint(0, 26)

    posicion_1 = letras[numero_aleatorio_1]

    cadena_mayusculas+=posicion_1.upper()
    #print(cadena_mayusculas)

    n_veces_uno+=1




############## minusculas ####################
generar_minusculas = input("Ingrese cantidad de letras minúsculas: ")
minusculas = int(generar_minusculas)

cadena_minusculas = []
n_veces_dos = 1
while n_veces_dos<=minusculas:

    numero_aleatorio_2 = random.randint(0, 26)

    posicion_2 = letras[numero_aleatorio_2]

    cadena_minusculas+=posicion_2
    #print(cadena_minusculas)

    n_veces_dos+=1



############## numeros ######################
generar_numeros = input("Ingrese cantidad de números: ")
numeros = int(generar_numeros)

cadena_numero = []
n_veces_tres = 1
while n_veces_tres<=numeros:
    numero_aleatorio_3 = random.randint(0, 99)

    cadena_numero.append(numero_aleatorio_3)
    #print(cadena_numero)
    
    n_veces_tres+=1



############## caracteres ###################
generar_caracteres = input("Ingrese cantidad de caracteres: ")
n_caracteres = int(generar_caracteres)

cadena_caracteres = []
n_veces_cuatro = 1
while n_veces_cuatro<=n_caracteres:
    numero_aleatorio_4 = random.randint(0, 13)

    posicion_4 = caracteres[numero_aleatorio_4]

    cadena_caracteres+=posicion_4
    #print(cadena_caracteres)

    n_veces_cuatro+=1
    

########## generacion de contraseña ############
contraseña = cadena_mayusculas+cadena_minusculas+cadena_numero+cadena_caracteres

random.shuffle(contraseña)

contraseña_cadena = str(contraseña)

contraseña_texto = ""
for i in contraseña_cadena:
    contraseña_texto += i
   

contraseña_final = ("").join(contraseña_texto)

print(f"Contraseña: {contraseña_final}")
