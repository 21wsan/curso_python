print('**** Lista y diccionarios ****')

personas = [
    {
    'nombre': 'angelica',
    'apellido': 'flores',
    'edad': '21'
    },

    {
    'nombre': 'alejandra',
    'apellido': 'reyes',
    'edad': '32'
    }
]
print(personas)

# acceder a un diccionario desde una lista
print(f'''Detalle del primer elemento de la lista

        Nombre: {personas[0].get('nombre')}
        Apellido: {personas[0].get('apellido')}
        Edad: {personas[0].get('edad')}
''')

# recorrer los elementos de la lista
print()
for contador, persona in enumerate(personas):
    print(f'{contador} - Persona: {persona}')
    # otra forma de acceder al detalle del diccionario
    # print(f'Detalle Nombre: {persona.get('nombre')}, Apellido: {persona.get('apellido')}, Edad: {persona.get('edad')}')