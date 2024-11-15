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