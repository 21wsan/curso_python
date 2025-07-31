print('*** PlayList de Canciones ***')

# creamos la lista vacía
lista_reproduccion = []

# agregar canciones
lista_reproduccion.append('Hotel California - Eagles')
lista_reproduccion.append('Staying Alive - Eagles')
lista_reproduccion.append('Dream on - Aerosmith')

# ordenar la lista en orden alfabetico con sort
lista_reproduccion.sort()
# lista_reproduccion.sort(reverse=True) para ordenar de forma descendente

# mostrar la lista de canciones
print(f'\nLista de Reproducción en Orden Alfabetico')
print(lista_reproduccion)

# mostrar la lista iterando sus elementos
print('\nIteramos el PlayList')
for cancion in lista_reproduccion:
    print(f'- {cancion}')