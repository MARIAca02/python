import random
import string

def generate_password(length):
    if length < 8:
        print("La longitud mínima de la contraseña debe ser 8.")
        return None
    
    password_characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(password_characters) for _ in range(length))
    
    # Asegurar que haya al menos un carácter de cada tipo
    while (not any(c.islower() for c in password) or
           not any(c.isupper() for c in password) or
           not any(c.isdigit() for c in password) or
           not any(c in string.punctuation for c in password)):
        password = ''.join(random.choice(password_characters) for _ in range(length))
    
    return password

def main():
    length = int(input("Ingrese la longitud de la contraseña (mínimo 8): "))
    password = generate_password(length)
    
    if password:
        print(f"Contraseña generada: {password}")
    else:
        print("La longitud ingresada es inválida.")

if __name__ == "_main_":
    main()