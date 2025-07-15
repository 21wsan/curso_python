print('*** Aplicacion de Salud y Fitness ***')

# constantes
META_PASOS_DIARIOS = 10000
CALORIAS_POR_PASO = 0.04 # valor aproximado, kilocalorias

# pedir valores al usuario
nombre_usuario = input('Cual es su nombre?:')
pasos_diarios = int(input('cuantos pasos has caminado hoy? '))

# verificar si el usuario alcanzo la meta
meta_alcanzada = pasos_diarios >= META_PASOS_DIARIOS
meta_alcanzada_txt = 'Si' if meta_alcanzada else 'No' # operador ternario

# realizar calculos
calorias_quemadas = pasos_diarios * CALORIAS_POR_PASO

# mostrar informacion
print(f'\nUsuario: {nombre_usuario}')
print(f'Pasos Dados Hoy: {pasos_diarios}')
print(f'Calorias Quemadas: {calorias_quemadas} kcal')
print(f'Meta de Pasos Alcanzada: {meta_alcanzada_txt}')
print(f'La Meta de Pasos Diarios Es: {META_PASOS_DIARIOS} pasos')