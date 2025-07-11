print('*** Sentecia If ***')

edad = int(input('Ingrese la edad: '))

if edad >= 18:
    print(f'Tienes {edad} años, eres mayor de edad')
elif 13 <= edad < 18:
    print(f'Tienes {edad} años, eres adolecente...')
else:
    print(f'Tienes {edad} años, eres menor de edad')