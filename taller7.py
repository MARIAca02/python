def calcular_valor_futuro(inversion_inicial, tasa_interes, años):
    """
    calcular el valor futuro de la inversion inicial.
    :parametros inversion_inicial:el valor inicial de la inversion (float)
    :parametros tasa_interes: la tasa de inters como decimal (float)
    :parametros años: el valor de años (int)
    return: el valor futuro de la inversion (float)
    """
    # Suponemos interés compuesto anual
    valor_futuro = inversion_inicial * (1 + tasa_interes)**años
    return valor_futuro

# Solicitar la información al usuario
inversion_inicial = float(input("Ingrese la inversión inicial: $"))
tasa_interes = float(input("Ingrese la tasa de interés anual (%): "))
años = int(input("Ingrese el número de años de la inversión: "))
inversion_inicial = 2000.0
tasa_interes = 2.5
años = 6 

# Calcular el valor futuro
valor_futuro = calcular_valor_futuro(inversion_inicial, tasa_interes, años)

# Mostrar el resultado
print(f"El valor futuro de la inversión será de: {valor_futuro:.2f}")