print('*** Cajero Automatico ***')

saldo = 1000
salir = False

while not salir: # mientras salir no sea verdadero
    print('''
    Operaciones que puedes realizar:\n
      1. Consultar saldo
      2. Retirar
      3. Depositar
      4. Salir
    ''')
    opcion = int(input('Escoje una opción: '))
    if opcion == 1:
        print(f'\nEl saldo actual es de: {saldo:.2f}')
    elif opcion == 2:
        retiro = float(input('Saldo a retirar: '))
        if saldo >= retiro:
            saldo -= retiro
            print(f'\nEl nuevo saldo es de: {saldo:.2f}')
        else:
            print(f'\nNo cuentas con el saldo suficiente, saldo actual {saldo:.2f}')
    elif opcion == 3:
        deposito = float(input('Saldo a depositar: '))
        saldo += deposito
        print(f'El nuevo saldo es de: {saldo:.2f}\n')
    elif opcion == 4:
        print('\nTransacción finalizada, gracias\n')
        salir = True
    else:
        print('\nOpcion invalida, selecciona otra opción: ')
else:
    print('Terminando la aplicación de cajero automatico....\n')