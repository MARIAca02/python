def es_palindromo(palabra):
    palabra_invertida = palabra[::-1]  # Convertir la palabra 

    if palabra == palabra_invertida:
        return True
    else:
        return False

# Solicitar la palabra al usuario
palabra_usuario = input("Ingresa una palabra para verificar:")

# Verificar si la palabra es un palíndromo
if es_palindromo(palabra_usuario):

# Mostrar el resultado

    print(palabra_usuario, "es un palíndromo.")
else:
    print(palabra_usuario, "no es un palíndromo.")