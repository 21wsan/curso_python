print("*** sistema de tienda Online ***")

# definir las variables de un producto

nombre_producto = "camara digital"
precio_producto = "399.99"
cantidad_inventario = 20
disponible_entrega = True

# mostrar información del porducto
print(f"Producto: {nombre_producto}")
print(f"Precio: ${precio_producto}")
print(f"Cantidad: {cantidad_inventario}")
print(f"Disponible: {disponible_entrega}")

# hacer cambios
precio_producto = 299.99
cantidad_inventario = 10
disponible_entrega = True

print()
print(f"Producto: {nombre_producto}")
print(f"Precio: ${precio_producto}")
print(f"Cantidad: {cantidad_inventario}")
print(f"Disponible: {disponible_entrega}")