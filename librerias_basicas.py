import os, json

#obtener la ruta actual del directorio
ruta = os.getcwd()
print(f"Mi ruta actual de trabajo es: {ruta}")

#crear una nueva carpeta en el directorio actual de trabajo
os.system("mkdir nueva_carpeta_2")

#para especificar la direccion
ruta_carpeta = ruta + "/python"
os.system("mkdir" + ruta_carpeta + "nueva_carpeta") #mkdir + la ruta + el nombre de la carpetas