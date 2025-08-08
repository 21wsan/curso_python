print('**** Diccionarios en Python ****')

# creamos un diccionario de persona con clave y valor
# los diccionarios no soportan valores duplicados
persona = {

    'nombre': 'Karla',
    'edad': 30,
    'ciudad': 'Colombia'
}

print(f'Diccionario de persona: {persona}')

# acceder a los elementos del diccionario
print(f'Nombre: {persona['nombre']}')
print(f'Edad: {persona.get('edad')}') # se solicita el valor de edad por medio del metodo get
print(f'Ciudad: {persona.get('ciudad')}')

# Modificar el valor del diccionario
persona['edad'] = 35 # sintaxis para cambiar el valor de un key en el diccionario
print(f'Diccionario de persona: {persona}')

# agregar un nuevo elemento al diccionario
persona['profesion'] = 'ingeniero' # sintaxis para agredar una nueva key (profesion) al diccionario.
print(f'Diccionario de persona: {persona}')

# eliminar un elemento del diccionario
del persona['ciudad']
print(f'Diccionario de persona: {persona}')

# Eliminar 2
persona.pop('profesion') # elimina el elemento del diccionario
print(f'Diccionario de persona: {persona}')

# Iterar los elementos del diccionario (llave, valor)
for llave, valor in persona.items():
    print(f'Llave: {llave}, Valor: {valor}')

# obtener los valores
print(f'\nvalores del diccionario')
for valor in persona.values():
    print(f'- valor: {valor}')

# obtener las llaves del diccionario
print(f'\nimpresion de las llaves del diccionario')
for llave in persona.keys():
    print(f'- {llave}')