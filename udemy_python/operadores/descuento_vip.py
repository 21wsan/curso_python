print('**** Sistema de Descuento ****')

NO_PRODUCTOS_DESCUENTO = 10

cantidad_productos = int(input('cuantos productos conpraste hoy?: '))
tiene_membresia = input('tiene membresia de la tienda (S/N)?: ')

es_elegible_descuento = (cantidad_productos >= NO_PRODUCTOS_DESCUENTO 
    and tiene_membresia.strip().lower() == 'si')

print(f'tiene acceso al descuento {es_elegible_descuento}')