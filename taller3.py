# Solicitar la cadena de texto al usuario
texto = input("Ingresa una cadena de texto: ")

# dividir el texto en palabras
palabras = texto.split()

# Contar la cantidad de palabras
cantidad_palabras = len(palabras)

# Mostrar el resultado
print(f"Las palabras en la cadena de texto '{texto}' contiene {cantidad_palabras}palabras.")