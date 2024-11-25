def nombre_funcion(parametro1: int, parametro2: str):  #para tipar la funcion especifico el tipo de variable | pueden ir parametros o no
    pass


def saludo(nombre: str):
    print("Hola " + nombre)

saludo("mi lord")

###########################
def es_primo(n):
    for i in range(2, n):
        if n%i == 0:
            return False
    return True

def numeros_primos(nums):
    primos = []
    for n in nums:
        if es_primo(n):
            primos.append(n)
    return primos      

numeros = [1, 8, 3, 9, 10, 25, 12, 33]
numeros_primos = numeros_primos(numeros)    
print(numeros)
print(numeros_primos)  

###########################
def pares_impares(numeros):
    pares = []
    impares = []
    for n in numeros:
        if (n%2 == 0):
            pares.append(n)
        else:
            impares.append(n)    

    return pares, impares


lista_numeros = [12, 45, 2, 1, 89, 90, 35]            
nums_pares, num_impares = pares_impares(lista_numeros)


#######################
#pasar datos a los parametros de las funciones

def suma(num1:int, num2:float)-> float:
   
    """funcion que recibe dos numeros y los suma

        Arg:
            num1 (int):numero entero
            num2 (int):numero decimal

        Return:
            float: resultado de la suma    
    """

    resultado = num1 + num2
    
    return resultado
        

#parametro por posicion:
x = suma(6, 10)
print(f"El resultado de la suma x es: {x}")

#parametro por referencia:
y = suma(num1=6, num2=10)
print(f"El resultado de la suma y es: {y}")


#######################################
#funcion como argumento de otra funcion
def squaere(num3: int)-> int:
    return num3*num3

def calculate(func, num):
    f = func(num)

    return x

n = int(input("Ingrese un numero entero: "))
square_number = calculate(squaere, n)
print(f"El cuadrado de {n} es: {square_number}")
                          

#funciones que agrupan funciones | metodos de la funcion
def operaciones_matematicas():
    #metodos de la funcion
    def plus(num6, num7, num8):
        return num6 + num7+ num8

    def restar(num6, num7):
        return num6 - num7

    def multiplicar(num6, num7, num8):
        return num6 * num7 * num8


j = 40
k = 10
p = 2

suma_nums = operaciones_matematicas.plus(j, k, p)