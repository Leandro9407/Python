nombres = list()

cont = 0
while cont<=10: 
    digitar = input("Ingrese nombres: ")
    nombres.append(digitar)
    cont+=1

print(f"Lista de nombres: {nombres}")    


conjunto = set(nombres)
lista = list(conjunto)

print(f"Lista filtrada: {lista}")