import random

def adivinar_numero():
    numero_correcto = random.randint(1, 100)
    intentos = 0
    max_intentos = 7
    adivinanza = 0

    print("¡Bienvenido al juego de adivinanza!")
    print("Estoy pensando en un número entre 1 y 100.")
    print(f"Tienes {max_intentos} intentos para adivinarlo.")

    while intentos < max_intentos:
        try:
            adivinanza = int(input("Adivina el número: "))
            intentos += 1

            if adivinanza < numero_correcto:
                print("El número es mayor.")
            elif adivinanza > numero_correcto:
                print("El número es menor.")
            else:
                print(f"¡Felicidades! Adivinaste el número en {intentos} intentos.")
                break
        except ValueError:
            print("Por favor, ingresa un número válido.")

    if intentos == max_intentos and adivinanza != numero_correcto:
        print(f"Lo siento, te quedaste sin intentos. El número era {numero_correcto}.")

if __name__ == "__main__":
    adivinar_numero()
