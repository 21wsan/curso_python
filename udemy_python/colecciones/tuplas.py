print('*** Manejo de Tuplas ***')

mi_tupla = (1,2,3,4,5)
print(mi_tupla)

# no se puede modificar una tupla, generalmente tiene () separado por (,)

# iterar los elementos de la tupla
for elemento in mi_tupla:
    print(elemento, end=' ')

# crear una tupla para una coordenada x,y

coordenadas = (3,5)
# accedemos a cada elemento de la tupla
print(f'\nCoordenada en el eje X: {coordenadas[0]}')
print(f'\nCoordenada en el eje Y: {coordenadas[1]}')

# crear una tupla unitaria
tupla_un_elemento = 10,
print(f'tupla de un elemento: {tupla_un_elemento}')

# tupla anidada
tupla_anidada = (1, (2,3), (4,5))
print(f'Segundo elemento de la tupla anidada: {tupla_anidada[1]}')
