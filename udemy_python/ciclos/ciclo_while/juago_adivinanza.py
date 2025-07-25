from random import randint

print('*** Juego adivinanzas ***')

numero_secreto = randint(1, 50)
intentos = 0
adivinanza = None
INTENTOS_MAXIMOS = 5

while adivinanza != numero_secreto and intentos < INTENTOS_MAXIMOS:
    adivinanza = int(input('Adivina el numero secreto (1 - 50): '))
    # agregar ayuda para orientar
    if adivinanza < numero_secreto:
        print('el numero secreto es mayor')
    elif adivinanza > numero_secreto:
        print('el numero secreto es menor')
    # incremento de variable intentos
    intentos +=1
if adivinanza == numero_secreto:
    print(f'felicidades adivinaste el numero secreto en {intentos} intentos')
else:
    print(f'Lo siento has agotado tus intentos máximos: {INTENTOS_MAXIMOS}')
    print(f'El número secreto era: {numero_secreto}')

