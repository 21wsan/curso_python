print('*** Creacion y validación de password ***')

password = input('Ingrese un password (debe tener al menos 6 caracteres: )')

# validar password
while len(password) < 6:
    print('La longitud no cumple con los requisitos, debe tener al menos 6 caracteres')
    password = input('Ingrese un nuevo valor de password: ')
else:
    print('El valor de password es válido')