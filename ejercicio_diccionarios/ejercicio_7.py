
datos_usuario = {}
datos = {}

for i in range(1):
        
    diligenciar_nombre = input("Escriba su nombre: ")
    datos_usuario.update({"Nombre":diligenciar_nombre})

    diligenciar_apellido = input("Escriba su apellido: ")
    datos_usuario.update({"Apellido":diligenciar_apellido})

    diligenciar_edad = input("Escriba su edad: ")
    datos_usuario.update({"Edad":diligenciar_edad})

    diligenciar_correo = input("Escriba su correo electrónico: ")
    datos_usuario.update({"Correo":diligenciar_correo})

    diligenciar_hijos = input("Escriba la cantidad de hijo: ")
    datos_usuario.update({"Hijos":diligenciar_hijos})

    print(datos_usuario) 

for y in datos_usuario:
    print(datos_usuario)

