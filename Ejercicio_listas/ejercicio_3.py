cadena = ['eiae', '1234', 'aoba', 'pijo', 'ojio', '4384', 'lnfq']
cont = 0

for i in cadena:
    if i[0]==i[-1]:
        cont+=1

print(f"Cadenas con la primera y ultima letra iguales: {cont}")        

