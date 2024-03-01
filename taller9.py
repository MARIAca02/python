import random

def main():
    number_a_adivinar = random.randint(1, 100)
    guess = None
    attempts = 0

    while guess != number_a_adivinar:
        guess = int(input("Intente adivinar el número entre 1 y 100: "))
        attempts += 1

        if guess < number_a_adivinar:
            print("Intente un número más grande.")
        elif guess > number_a_adivinar:
            print("Intente un número más pequeño.")
    
    print(f"¡Felicidades! Adivinaste el número en {attempts} intentos.")

if __name__ == "_main_":
    main()