print('**** Lista de Suscriptores ****')

# definimos el set inicial, vacío
# suscriptores = {} aqui se define un diccionario vacio, no un set,
#  por lo tanto esta opción no es valida para set
suscriptores = set() # forma correcta para definir un set vacío
numero_suscriptores = int(input('Indica el numero de suscriptores inicial: '))
for _ in range(numero_suscriptores):
        suscriptores.add(input('nuevo suscriptor (Email): '))

print(f'Lista de suscriptores inicial: {suscriptores}\n')

# verificar si el nuevo suscriptor ya esta en la lista
nuevo_suscriptor = input('indica el nuevo suscriptor: ')
if nuevo_suscriptor in suscriptores:
    print(f'El nuevo suscriptor {nuevo_suscriptor} ya esta en la lista {suscriptores}')
else:
    suscriptores.add(nuevo_suscriptor)
    print(f'El nuevo suscriptor {nuevo_suscriptor} se ha agregado a la lista')
print(suscriptores)

# eliminar un suscriptor
suscriptor_eliminar = input('Indica el suscriptor a eliminar: ')
suscriptores.remove(suscriptor_eliminar)
print(f'\nEl suscriptor {suscriptor_eliminar} ha sido eliminado de la lista')
print(f'lista de suscriptores {suscriptores}')

# verificar la cantidad total de suscriptores
print(f'Cantidad de suscriptores: {len(suscriptores)}')

# mostrar todos los suscriptores
print('---- lista de suscriptores ----')
for suscriptor in suscriptores:
    print(f'- {suscriptor}')