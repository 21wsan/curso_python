print("\n*** Calculadora en Python ***")

# num1 = num2 = 0, 0  para definil multiples variables estan las opciones de la linea 3 y 4
num1,num2 = 0, 0
salir = False

while not salir:
    print('''
        Operaciones que puedes realizar
          1. Suma
          2. Resta
          3. Multiplicación
          4. División
          5. Salir''')
    opcion = int(input('\nEscoje una opción: '))
    if 1 <= opcion <= 4:
            num1 = float(input('\nIngrese el primer valor: '))
            num2 = float(input('Ingrese el segundo valor: '))
    if opcion == 1:
        print('\n*** Opcion Sumar ***\n')
        resultado = num1 + num2
        print(f'\nEl resultado de la suma es: {resultado}')
    elif opcion == 2:
        print('\n*** Opcion Restar ***\n')
        resultado = num1 - num2
        print(f'\nEl resultado de la resta es: {resultado}')
    elif opcion == 3:
        print('\n*** Opcion Multiplicar ***\n')
        resultado = num1 * num2
        print(f'\nEl resultado de la multiplicacion es: {resultado}')
    elif opcion == 4:
        print('\n*** Opcion Dividir ***\n')
        resultado = num1 / num2
        print(f'\nEl resultado de la division es: {resultado:.2f}')
    elif opcion == 5:
        print('\n*** Cerrando Calculadora ***\n')
        salir = True
    else:
        print('Opcion Invalida, seleccione de nuevo')
else:
    print('Aplicación terminada\n')
    


        