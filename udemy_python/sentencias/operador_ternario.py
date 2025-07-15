print('*** Operador Ternario ***')

edad = int(input('Cual es tu edad: '))

# si la edad es mayor o igual que 18 devuelve 'Si' si no lo es devuelve 'No'
es_adulto = 'Si' if edad >= 18 else 'No'
print(f'Es un adulto?: {es_adulto}')