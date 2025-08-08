print('**** Manejo de Sets ****')

# crear un conjunto
# un set siempre va dentro de {llaves} no almacena ningun orde
#  e ignora los elementos repetidos
mi_set={1,2,3,4,5,4}
print(f'Mi set: {mi_set}')

# agregar elementos al set = los set son de tipo mutable similar a las listas
#  por lo que se pueden agregar elementos.
mi_set.add(6)
mi_set.add(7)
print(f'Mi set modificado: {mi_set}')

# intentar agregar un elemento duplicado
mi_set.add(3)

# eliminar elementos de un conjunto - en set no se trabaja sobre un indice
mi_set.remove(4)
print(f'Mi set modidicado: {mi_set}')

# iterar los elementos del set
for elemento in mi_set:
    print(elemento, end = ' ')

# comprobar si existe un elemento en el set
print(f'\nExiste el valor de 4 en el set?: {1 in mi_set}')
# {1 in mi_set} se puede usar en listas, tuplas y set

# obtener longitud del set
print(f'Longitud del conjunto: {len(mi_set)}')