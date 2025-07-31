print('*** Manejo de listas ***')

# ejemplo de listas en python, comienzan con []
mi_lista = [1,2,3,4,5]
print(f'{mi_lista} -> lista original')

# largo de una lista
print(f'Largo de la lista = {len(mi_lista)}')

# Acceder a los elementos de la lista por indice
print(f'valor del indice 4 = {mi_lista[4]}')
print(f'valor del ultimo indice = {mi_lista[-1]}')

# Modificar los elementos de una lista
mi_lista[1] = 10
print(f'{mi_lista} Modificamos el valor del indice 1 = {mi_lista[1]}')

# Agregar un nuevo elemento al final de la lista
mi_lista.append(6)
print(f'{mi_lista} se agrego el elemento 6')

# añadir un nuevo elemento en un indice especifico
mi_lista.insert(2,15)
print(f'{mi_lista} -> Se añadio el valor de 15 en el indice 2')

# Eliminar elementos de una lista
# usando el metodo remove
mi_lista.remove(5) # elimina de la lista el valor 5
print(f'{mi_lista} -> se removio el valor 5')

# Removemos por indice con el metodo pop
mi_lista.pop(1) # remueve el elemento del indice 1
print(f'{mi_lista} -> se elimino el indice 1')

# eliminar usando la palabra del (delete)
del mi_lista[2]
print(f'{mi_lista} -> se elimino el indice 2')

# Obtener sublistas
sublista = mi_lista[1:3] # genera una sublista del indice 1 al 2 (3 no se incluye)
print(f'Sublista [1:3] {sublista}')
