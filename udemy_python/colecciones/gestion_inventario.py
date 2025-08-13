print('**** Gestion de Inventario ****')

inventario = []

numero_producto = int(input('Cuantos productos deseas agregar al inventario: '))
for indice in range(numero_producto):
    print(f'Proporciona los valores del producto {indice + 1}')
    nombre = (input('Nombre: '))
    precio = float(input('Precio: '))
    cantidad = int(input('Cantidad: '))
    # creamos el diccionario con el detalle del producto
    producto = {'id': indice, 'nombre': nombre, 'precio': precio, 'cantidad': cantidad}
    # agregamos el nuevo producto al inventario
    inventario.append(producto)

# mostrar el inventario inicial
print(f'\nInventario inicial: {inventario}')

# buscar un producto por id
id_buscar = int(input(f'\nIngresa el id del producto a buscar: '))
producto_encontrado = None
for producto in inventario:
    if producto.get('id') == id_buscar:
        producto_encontrado = producto
        break

if producto_encontrado is not None:
    print(f'Informacion del producto encontrado: ')
    print(f'''Id: {producto_encontrado.get('id')}
    Nombre: {producto_encontrado.get('nombre')}
    Precio: {producto_encontrado.get('precio')}
    Cantidad: {producto_encontrado.get('cantidad')}''')
else:
    print(f'Producto con Id: {id_buscar} No encontrado')

# mostrar el inventario detallado
print('\n---- Inventario detallado ----')
for producto in inventario:
    print(f'''Id: {producto.get('id')}
    Nombre: {producto.get('nombre')}
    Precio: ${producto.get('precio'):.2f}
    Cantidad: {producto.get('cantidad')}''')