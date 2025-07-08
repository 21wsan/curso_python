print('**** Sistema Prestamo de Libros ****')

DISTANCIA_PERMITIDA = 3

tiene_credencial = input('tiene credencial de estudiante (Si/No): ')
distancia = int(input('a cuantos KM vive de la biblioteca: '))

es_elegible_prestamo = (tiene_credencial.strip().lower() == 'si' 
                        or distancia <= DISTANCIA_PERMITIDA)

print(f'es elegible para prestamo de libros? {es_elegible_prestamo}')