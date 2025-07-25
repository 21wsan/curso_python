print('*** Sistema de administración de cuentas ***')

salir = False
while not salir:    # mientras salir no sea verdadero sigue iterando
    print('''Menu:
    1.Crear cuenta:
    2.Eliminar cuenta:
    3.Salir:
    ''')
    opcion = int(input('Escoje una opción: '))
    if opcion == 1:
        print('\nCreando la cuenta...\n')
    elif opcion == 2:
        print('\nBorrando la cuenta...\n')
    elif opcion == 3:
        print('\nSaliendo del sistema, hasta pronto!\n')
        salir = True
    else:
        print('Opcion incorrecta, proporciona una opción: \n')
else:
    print('Terminando el sistema de administración de cuentas...\n')