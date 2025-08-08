print('**** Combinacion de Listas y Tuplas ****')

# definir una lista que almacena tuplas de productos
# productos es una lista
productos = [
    ('P001', 'Camiseta', 20.00), # esto es un elemento de la lista que contiene una tupla
    ('P002', 'Pantalon', 30.00),
    ('P003', 'Sudadera', 40.00)
]

# Imprimir la información de cada producto y el precio total
precio_total = 0
print('Información de los productos')
for producto in productos:
    # print(producto)
    id, descipcion, precio = producto # unpacking
    print(f'ID = {id}, DESCRIPCION = {descipcion}, PRECIO = ${precio}')
    precio_total += precio # producto[2]
print(f'Precio total de los productos = ${precio_total}')


