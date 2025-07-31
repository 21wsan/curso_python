print('*** Impresion de Mensaje ***')

mensaje = input('Proporciona el mensaje a repetir: ')
numero_repeticiones = int(input('Proporciona el numero de repeticiones: '))

# iterar sobre el rango de repeticiones
for i in range(numero_repeticiones):
    print(f'{i+1} - {mensaje}')

'''
    for _ in range(numero_repeticiones):
        print(f'{i+1} - {mensaje}')
    el guion indica que no usaremos la variable i dentro del for
'''