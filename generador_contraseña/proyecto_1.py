import random

letras = ("a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "ñ", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z")

caracteres = ("!", "+", "-", "_", "*", "/", "?", "=", "#", "$", "%", "&", "¡", "¿")

mayus = False
minus = False
number = False
caract = False

opcion = 0
while opcion==0 or opcion==1 or opcion==2 or opcion==3 or opcion==4 or opcion==5:

       
    print("|----------  GENERADOR DE CONTRASEÑA -----------|")
    print("|                                               |")
    print("|  1. indicar cantidad de mayúsculas            |")
    print("|  2. indicar cantidad de minúsculas            |")
    print("|  3. indicar cantidad de números               |")
    print("|  4. indicar cantidad de caracteres            |")
    print("|  5. Generar contraseña                        |")
    print("|-----------------------------------------------|")
    opcion = int(input("ingrese opcion: "))
    print("")

    if opcion==1:  #mayuscula

        generar_mayusculas = input("Ingrese cantidad de letras mayúsculas: ")
        mayusculas = int(generar_mayusculas)

        cadena_mayusculas = ""
        n_veces_uno = 1    
        while n_veces_uno<=mayusculas:
            numero_aleatorio_1 = random.randint(0, 26)

            posicion_1 = letras[numero_aleatorio_1]

            cadena_mayusculas+=posicion_1.upper()
            n_veces_uno+=1   
            mayus = True
            

    if opcion==2:   #minuscula
        generar_minusculas = input("Ingrese cantidad de letras minúsculas: ")
        minusculas = int(generar_minusculas)

        cadena_minusculas = ""
        n_veces_dos = 1
        while n_veces_dos<=minusculas:

            numero_aleatorio_2 = random.randint(0, 26)

            posicion_2 = letras[numero_aleatorio_2]
        
            cadena_minusculas+=posicion_2
            n_veces_dos+=1
            minus = True
    
            
    if opcion==3:  #numeros
        generar_numeros = input("Ingrese cantidad de números: ")
        numeros = int(generar_numeros)

        cadena_numero = ""
        n_veces_tres = 1
        while n_veces_tres<=numeros:
            numero_aleatorio_3 = random.randint(0, 9)

            cadena_numero+=str(numero_aleatorio_3)         
            n_veces_tres+=1   
            number = True    
            

    if opcion==4:   # caracteres
        generar_caracteres = input("Ingrese cantidad de caracteres: ")
        n_caracteres = int(generar_caracteres)

        cadena_caracteres = ""
        n_veces_cuatro = 1
        while n_veces_cuatro<=n_caracteres:
            numero_aleatorio_4 = random.randint(0, 13)

            posicion_4 = caracteres[numero_aleatorio_4]

            cadena_caracteres+=posicion_4
            n_veces_cuatro+=1
            caract = True
        

    if opcion==5 and mayus==True and minus==True and number==True and caract==True:   #constraseña final
        union_contraseña = cadena_mayusculas+cadena_minusculas+cadena_numero+cadena_caracteres

        convertir_lista = list(union_contraseña)
        random.shuffle(convertir_lista)

        contraseña = ""
        for i in convertir_lista:
            contraseña += i
        
        contraseña_final = ("").join(contraseña)


        print(f"Contraseña: {contraseña_final}")
        
        break

    elif opcion==5:
        print("FALTAN CAMPOS POR LLENAR:")
        if mayus==False:
            print("Campo de mayúsculas: opcion 1")
    
        if minus==False:    
            print("Campo de minúsculas: opcion 2")
            
        if number==False:
            print("Campo de números: opcion 3")
            
        if caract==False:
            print("Campo de caracteres: opcion 4")
            
    print("")
