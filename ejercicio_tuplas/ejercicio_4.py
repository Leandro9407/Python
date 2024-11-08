tupla = (1, 2, 3, 4, 5, 6, 4, 7, 4, 8, 9, 4)

determinar = int(input("Digite número a encontrar (1 a 10): "))

cont = 0
for i in tupla:
    if determinar==i:
        cont+=1

print(f"El número {determinar} se encontro {cont} veces")
