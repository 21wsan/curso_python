print('**** Generación Ticket de Venta ****')

p_leche = float(input('Precio Leche: '))
p_pan = float(input('Precio Pan: '))
p_lechuga = float(input('Precio Lechuga:'))
p_tomate = float(input('Precio Tomate: '))
descuento_porcentaje = int(input('desea aplicar algún descuento (%)?: '))
# calculo de subtotal (sin impuestos)
subtotal = p_leche + p_pan + p_lechuga + p_tomate

# aplicar descuento
descuento = subtotal * (descuento_porcentaje/100)

# subtotal con descuento

subtotal_con_descuento = subtotal - descuento

# calculo con impuestos (16%)

impuesto = subtotal_con_descuento * 0.16

# calculo total de la compra con impuestos
costo_total_compra = subtotal_con_descuento + impuesto
print(f'''
Subtotal: ${subtotal:.2f}
Descuento: ${descuento} ({descuento_porcentaje}%)
Subtotal con Descuento: ${subtotal_con_descuento}
Impuesto (16%): ${impuesto:.2f}
Costo total de la compra: {costo_total_compra:.2f}
''')