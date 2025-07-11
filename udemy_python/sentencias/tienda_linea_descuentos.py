print('*** Sistema de Descuentos ***')

compra = int(input('Cual fue el monto de la compra?: '))
es_miembro_tienda = input('Es miembro de la tienda (SI/NO): ')

if compra >= 10000 and es_miembro_tienda == 'si'.strip().lower:
    print(f'Felicidades su compra tiene un descuento del 10%')
elif es_miembro_tienda == 'si'.strip().lower():
    print('Felicidades su compra tiene un descuento del 5%')
else:
    print('su compra no aplica para descuentos')