print('*** Suma Acumulativa ***')

# sumar los primeros 5 numeros
MAXIMO = 5
numero = 1
acumulador_suma = 0

# comenzar a iterar
while numero <= MAXIMO:
    # imprimir lo que se va a sumar
    print(f'(acumulador_suma + numero) -> {acumulador_suma} + {numero}')
    acumulador_suma += numero
    numero += 1

    # resultado de la suma parcial
    print(f'Suma parcial acumulada: {acumulador_suma}\n')
print(f'\nResultado de la suma acumulada: {acumulador_suma}')