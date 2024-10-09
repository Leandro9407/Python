num_1 = 10
num_2 = 20
text_1 = 'Hola'
text_2 = 'Clase'

dia = 2

suma = num_1 + num_2

# print(num_1, num_2, sep='+', end='=')  #SEP: separa las variables, END: para poner al final
# print(suma)
# print(text_1, text_2)
# print('Hoy es ' + str(dia) + ' octubre')  #STR sirve para cambiar un INT a STRING


# #impresion con formato:
# message = 'El día {} tenemos que enviar {} ejercicios de física'  #para inyectar una variable
# print(message.format('lunes', 4))

# mensaje = 'imprimir {0:1f} de los {1:2d} números que hay' #primera posicion, enteros, decimales
# print(mensaje.format(123.12, 321)) 


# #impresion con nuevo formato
# day = 23
# cakes = 2
# print(f"El día {day} tenemos que traer {cakes} tortas") #interpolas: rezplazar las variables

# print("""Se usan tres comillas dobles
#       para un texto largo de varias
#       lineas""")

# print(type(num_1)) #para saber que tipo de variables es
# print("La variable text_1 es de tipo",type(text_1))

# print(f"La variable text_2 es de tipo {type(text_2)}")
# print("La variable num_2 es de tipo {}".format(type(num_2)))


# #funcion input() todo lo que devuelve la funcion input es STRING
# nombre = input("Ingresa tu nombre: ")
# print(f"Hola {nombre}, en que puedo ayudarte")

# numero_primero = input("Ingresa tu edad: ")
# print(f"La edad del bastardo {nombre} es {numero_primero}")

# #Si quiero el input sea un numero debo decir: int() o variable = int(input("   "))
# primer_numero = int(input("Ingrese numero: "))
# segundo_numero = int(input("Ingrese otro numero: "))

# print(f"La suma de {primer_numero} y {segundo_numero} es: {primer_numero+segundo_numero}")

#find() para encontrar caracteres, la encuentra como la posicion de un array
correo = "peloticas_calientes@gmail.com"
encontrar = correo.find("@")
print(f"Es una correo electrónico, @ detectado en la posicion: {encontrar}")

#dir para saber todo lo que se puede hacer con esa clase
print(dir(correo))

#split sirve para dividir las palabras dependiendo lo que encuentre
print("*"*64) #para hacer la cantidad de "" que quiero
texto = "Hoy hace mucho calor"
division_texto = texto.split(" ") #por espacio
print(f"\Texto original es {texto}")
print(f"\Texto dividido igual a = {division_texto}")

#join para unir el string
texto_unido = ("").join(division_texto)
print (f"{texto_unido}")
