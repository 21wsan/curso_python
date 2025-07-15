print('*** Sistema Tienda con Descuentos ***')

MONTO_COMPRA_DES = 10000

compra = float(input('Cual fue el monto de la compra?: '))
es_miembro = input('Es miembro de la tienda (SI/NO): ')

descuento = 0
# verificar
if compra >= MONTO_COMPRA_DES and es_miembro.strip().lower() == 'si':
    descuento = 0.1 # descuento del 10%
elif es_miembro.strip().lower() == 'si':
    descuento = .05 # descuento del 5%
elif compra >= MONTO_COMPRA_DES:
    descuento = .03 #descuento del 3%
else:
    descuento = 0

# hacer calculos respectivos
if descuento != 0:
    monto_descuento = compra * descuento
    monto_final = compra - monto_descuento
    print(f'Felicidades, has obtenido un descuento del {descuento * 100:.0f}%')
    print(f'Monto de la compra: ${compra:.2f}')
    print(f'Monto del descuento: ${monto_descuento:.2f}')
    print(f'Monto final de la compra con descuento: ${monto_final}')
else:
    print(f'\nNo obtuviste ningun tipo de descuento')
    print('Te invitamos a hacerte miembro de la tienda')
    print(f'Monto final de la compra: {compra}')