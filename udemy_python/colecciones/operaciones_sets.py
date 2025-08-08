print('**** Operaciones con Set ****')

a = {1,2,3,4}
b = {3,4,5,6}

# unir dos set con pipe |
union = a | b
print(f'Union de (a | b) : {union}')

# interseccion
# son los valores que se repiten el los 2 conjuntos de sets
interseccion = a & b
print(f'Interseccion de a & b = {interseccion}')

# diferenci
diferencia = a - b
print(f'direrencia a - b {diferencia}')