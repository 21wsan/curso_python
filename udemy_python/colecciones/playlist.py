print('*** PlayList de Canciones ***')

# creamos la lista vacía
lista_reproduccion = []

numero_canciones = int(input('Cuantas canciones deseas agregar?: '))

# iteramos cada elemento de la lista para agregar un nuevo elemento
for indice in range(numero_canciones):
    cancion = input(f'Proporciona la cancion {indice + 1}: ')
    lista_reproduccion.append(cancion)

# ordenar la lista en orden alfabetico con sort
# lista_reproduccion.sort(reverse=True) para ordenar de forma descendente
lista_reproduccion.sort()

# mostrar la lista iterando sus elementos
print('\nIteramos el PlayList\n')
for cancion in lista_reproduccion:
    print(f'- {cancion}')