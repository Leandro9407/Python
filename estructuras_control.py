#estructuras de control
#condicionales:

#if

a = 2
b = 5
c = None

if 1==2:
    print("Si")
else: 
    print("No")    

print("\n")

if a<b:
    print(f"{a} es menor que {b}")
elif b==a:
    print(f"{a} es igual que {b}")
else:
    print(f"{a} es mayor que {b}")        

print("\n")

#para que identifique si la variable esta vacia
if c:
    print(f"c = {c}")
else:
    print("No existe")    

   
#for

for i in range(10, 1): #longitud e incremento
    print(i)

for y in range(10, 20, 2): #inicializar, longitud, incremento
    print(f"y = {y}")

for l in 'texto': #interpreta el string como un array. cada letra esta en array
    print(l)    


###########################################
# while
d = 1

while d<=10:
    print(d)
    d+=1  

      





