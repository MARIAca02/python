def es_primos(numeros_primos):
    if numeros_primos < 2:
        return False
    for i in range(2, numeros_primos):
        
        if numeros_primos % i == 0:
            return False
    return True

def primeros_n_primos(n_usuario):
    numeros_primos = []
    cont = 0
    numeros_primos = 2
    
    while cont < n_usuario:
        if es_primos(numeros_primos):
            numeros_primos.append(numeros_primos)
            cont += 1
        numeros_primos += 1

    return numeros_primos


# Solicitar la cantidad de números al usuario
n_usuario = int(input("Ingresa la cantidad de números primos que deseas generar: "))

numeros_primos = primeros_n_primos(n_usuario)
for numeros_primos in numeros_primos:

# Mostrar el resultados
    print(f"Los primeros {n_usuario} números primos son: {numeros_primos}")