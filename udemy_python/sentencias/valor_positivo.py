print('*** Revisión de Valor Positivo***')

numero = int(input('Ingrese un numero: '))

if numero > 0:
    print(f'El numero {numero} es positivo')
elif numero < 0:
    print(f'El numero {numero} es negativo')
else:
    print(f'El numero es {numero}')