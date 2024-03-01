# lista de compras
lista_compras = []

# Función para agregar un elemento 
def agregar_elemento():
    elemento = input("Ingresa el elemento que deseas agregar a la lista de compras: ")
    lista_compras.append(elemento)
    print(f"{elemento} ha sido agregado a la lista de compras.")

# Función para mostrar 
def mostrar_lista():
    print("Lista de compras actual:")
    for elemento in lista_compras:
        print(elemento)

# Función para eliminar 
def eliminar_elemento():
    if not lista_compras:
        print("La lista de compras está vacía. No hay elementos para eliminar.")
        return
    
    elemento = input("Ingresa el elemento que deseas eliminar de la lista de compras: ")
    
    if elemento in lista_compras:
        lista_compras.remove(elemento)
        print(f"{elemento} ha sido eliminado de la lista de compras.")
    else:
        print(f"{elemento} no se encuentra en la lista de compras.")

# Menú principal
while True:
    print("\nGestión de lista de compras:")
    print("1. Agregar un elemento")
    print("2. Mostrar la lista de compras")
    print("3. Eliminar un elemento")
    print("4. Salir")

    opcion = input("Ingresa el número de la opción que deseas realizar: ")

    if opcion == "1":
        agregar_elemento()
    elif opcion == "2":
        mostrar_lista()
    elif opcion == "3":
        eliminar_elemento()
    elif opcion == "4":
        print("¡Hasta luego! Gracias por usar la gestión de lista de compras.")
        break
    else:
        print("Por favor, ingresa una opción válida (1-4).")