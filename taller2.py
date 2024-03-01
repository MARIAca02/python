def generar_secuencia_fibonacci(n):
    secuencia = [0,1]
    for i in range(2, n):
       siguiente_numero = secuencia[i-1] + secuencia[i-2]
       secuencia.append(siguiente_numero)
    return secuencia
n = int(input("ingrese el numero secuencia fibonacci a generar:"))
secuencia_fibonacci = generar_secuencia_fibonacci(n)
print("los primeros {}numeros de la secuencia fibonacci son{}".format(n,secuencia_fibonacci))