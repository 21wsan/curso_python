print('*** Sistema Reserva Hotel ***')

vista_mar_si = 190.50
vista_mar_no = 150.50

nombre = input('Ingrese su nombre?: ')
dias_estancia = int(input('Cuantos días se quedara en el hotel?: '))
vista_al_mar_txt = input('Desea cuarto con vista al mar? (Si/No): ')
vista_al_mar = vista_al_mar_txt.strip().lower() == 'si'

# calcular tarifas
if vista_al_mar:
    costo_total = dias_estancia * vista_mar_si
else:
    costo_total = dias_estancia * vista_mar_no
    

print('\n----- Detalles de la Reservación -----')
print(f'Nombre del cliente: {nombre}')
print(f'Dias de Estancia en el Hotel: {dias_estancia}')
#print(f'Cuarto con vista al mar: {vista_al_mar}')
print(f'Cuarto con vista al mar: ', 'Si' if vista_al_mar else 'No')
print(f'Valor total de la estadia: ${costo_total:.2f}')
print
print()
