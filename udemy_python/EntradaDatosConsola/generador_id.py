from random import randint

print('**** Generador de Id Unico ****')

name = input('Ingrese el nombre: ')
last_name = input('Ingrese el apellido: ')
year = input('Ingrese el año de Nacimiento (YYYY): ')

# normalizar valores
name_2 = name.strip().upper()[0:2]
last_name_2 = last_name.upper()[0:2]
year = year[2:]

# numero aleatorio
random = randint(1000,9999)

# generar el ID unico
ID = (f'{name_2}{last_name_2}{year}{random}')
# para usar una cadena multilinea se debe agregar triple comilla ej: (''' cadena multilinea ''')
print(f'''\nHola {name},
       su nuevo numero de identificación (ID) es: {ID}
        gracias...''')