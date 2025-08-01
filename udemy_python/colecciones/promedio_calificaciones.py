print('*** Promedio Calificaciones ***')
numero_calificaciones = int(input('Ingrese el numero de calificaciones a evaluar: '))
calificaciones = []

# iterar las calificaciones
for indice in range(numero_calificaciones):
    calificacion = float(input(f'Ingrese la calificación [{indice}] : '))
    calificaciones.append(calificacion)
    
# imprimir calificaciones
print(f'\nLas calificaciones proporcionadas son: {calificaciones}')

# calcular el promedio de calificaciones
# funcion sum(iterable) para sumar todos los elementos de una lista
suma_calificaciones = sum(calificaciones)
promedio = suma_calificaciones / numero_calificaciones
print(f'\nPromedio de calificaciones: {promedio:.2f}')

# usando un for para iterar y realizar la suma de calificaciones y promedio
suma = 0
for valor in calificaciones:
    suma += valor


promedio2 = suma / numero_calificaciones    
print(f'promedio 2 es: {promedio2}')