print('**** Lista de Suscriptores ****')

suscriptores = {'luisa@mail.com', 'sofira@mail.com', 'adriana@correo.com'}
print(f'Lista de suscriptores inicial: {suscriptores}\n')

# verificar si el nuevo suscriptor ya esta en la lista
nuevo_suscriptor = 'laura@mail.com'
if nuevo_suscriptor in suscriptores:
    print(f'El nuevo suscriptor {nuevo_suscriptor} ya esta en la lista {suscriptores}')
else:
    suscriptores.add(nuevo_suscriptor)
    print(f'El nuevo suscriptor {nuevo_suscriptor} se ha agregado a la lista')
print(suscriptores)

# eliminar un suscriptor
suscriptor_eliminar = 'luisa@mail.com'
suscriptores.remove(suscriptor_eliminar)
print(f'\nEl suscriptor {suscriptor_eliminar} ha sido eliminado de la lista')
print(f'lista de suscriptores {suscriptores}')

# verificar la cantidad total de suscriptores
print(f'Cantidad de suscriptores: {len(suscriptores)}')

# mostrar todos los suscriptores
print('---- lista de suscriptores ----')
for suscriptor in suscriptores:
    print(f'- {suscriptor}')