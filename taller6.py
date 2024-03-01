import random
#comentar
def lanzar_dados():
    dado1 = random.randint(1, 6)
    dado2 = random.randint(1, 6)
    return dado1, dado2

# Mostrar el resultado

def mostrar_resultados(dado1, dado2):
    print(f"Resultado del primer dado: {dado1}")
    print(f"Resultado del segundo dado: {dado2}")

# Simular el lanzamiento de dos dados
def simular_lanzamiento_dados():
    dado1, dado2 =lanzar_dados()
    mostrar_resultados(dado1, dado2)
    
simular_lanzamiento_dados()