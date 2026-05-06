# =========================
# PROYECTO 2: ADIVINA EL NÚMERO
# =========================

import random

numero_secreto = random.randint(1, 100)
intentos = 0

print("\nJuego: Adivina el número (1-100)")

while True:
    intento = int(input("Introduce tu número: "))
    intentos += 1

    if intento < numero_secreto:
        print("Demasiado bajo")
    elif intento > numero_secreto:
        print("Demasiado alto")
    else:
        print(f"¡Correcto! Lo lograste en {intentos} intentos")
        break
