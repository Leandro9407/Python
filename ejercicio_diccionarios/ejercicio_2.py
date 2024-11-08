diccionario = {"cinco":5, "tres":3, "uno":1, "cuatro":4, "dos":2}

ordenar = sorted(diccionario.items(), key=lambda item: item[1])
print(f"Ordenada en ascendente con key=lambada: {ordenar}")

##############################################
