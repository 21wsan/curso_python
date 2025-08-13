print('**** Agenda de contactos ****')

# tenemos un dicionario de diccionarios con key - value, con datos de los usuarios
agenda = {
    'carlos': {
        'telefono': '55667733',
        'email': 'carlos@correo.com',
        'direcion': 'calle falsa 123'
    },

    'maria': {
        'telefono': '9887766',
        'email': 'maria@email.com',
        'direccion': 'calle transilvania 132'
    },

    'pedro': {
        'telefono': '557733388',
        'email': 'pedro@correo.com',
        'direccion': 'av siempre viva'
    }
}

print(agenda)

# acceder a la informacion de un contacto en especifico
print(f'''la informacion de contacto de maria:
    telefono: {agenda['maria']['telefono']}
    email:{agenda['maria']['email']}
    direccion: {agenda.get('maria').get('direccion')}
''')

# agregar un nuevo contacto
agenda['sofia']= {
    'telefono': '19283746',
    'email': 'sofia@email.com',
    'direccion': 'calle del salvador 354'
}

print(agenda)

# eliminar un contacto existente
# se puede usar cualquiera de las siguientes opciones
agenda.pop('pedro')
# del agenda['pedro']
print(agenda)

# mostrar los contactos en la agenda con un ciclo for
for nombre, detalles in agenda.items():
    print(f'''Nombre: {nombre}
    Telefono: {detalles.get('telefono')}
    Email: {detalles.get('email')}
    Direccion: {detalles.get('direccion')}
    ''')