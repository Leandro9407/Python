#crear un diccionario 
dict_1 = dict()

#usando asignacion de la llave principal
capitales = dict(
        Colombia='Bogota',
        Venezuela= 'Caracas'
)
print(capitales)

#diccionario vacio
diccionario = {}

#crear un diccionario con llaves y valores
diccion = {
        "clave_1":1,
        "clave_2":2, 
        "clave_3":"red"
        }

#diccionario con varias estructuras de datos
color = {"colo_1":["Azul", "Verde"],
        "color_2":("amarillo", "morado")}

#diccionario dentro de otro diccionario
personas = {
            "barrio_1":[{
                "nombre":"pepito",
                "dirrecion":5,
                "telefono":4546546}],
                     
            "barrio_2":[{
                 "nombre":"fico"}]}


#llamar el valor de la llave
print(diccion['clave_2'])

#añadir nueva llave y valor
diccion["clave_4"] = 4
print(diccion)

#para remover llave
del diccion["clave_1"]

#get forma elegante de traer informacion
traer = diccion.get("clave_3", "llave encontrada") #le puedo configurar un mensaje de salida
print(traer)

#actualizar un elemento, si no esta la llave la crear
diccion.update({"clave_2":10})
print(diccion)

#eliminar el elemento
capitales.pop("Venezuela")
print(capitales)

#extraer las llaves
keys = diccion.keys()
print(keys)

#extraer los valores
values = diccion.values()
print(values)

#trear una tupla con llave y valor
items = diccion.items()
print(items)

#clear para eliminar todo el diccionario
amigas = {
    "mujer_1":"susana",
    "mujer_2":"yuyeimi"
}
amigas.clear()
print(amigas)

#sorted imprimir por los valores


#######################################################


keys_2 = ['Ten', 'Twenty', 'Thirty']
values_2 = [10, 20, 30]
juntos = {"fdaf"}

for i in range(1):
    juntos.update(keys_2)
    

    print(juntos)







