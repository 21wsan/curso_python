print('*** Sistema de Envios ***')

# constantes
NACIONAL = 10000
INTERNACIONAL = 20000

destino_envio = input('El envío es Nacional o Internacional (N/I): ')
peso = float(input('Cual es el peso del paquete a enviar en (Kg)?: '))
destino = None

# destino

if destino_envio.strip().upper() == 'N':
    destino = 'Nacional'
    valor = peso * NACIONAL
elif destino_envio.strip().upper() == 'I':
    destino = 'Internacional'
    valor = peso * INTERNACIONAL
else:
    print('Destino no valido...')    

# imprimir datos
print(f'Tipo de envio: {destino}')
print(f'costo de envio: {valor}')

