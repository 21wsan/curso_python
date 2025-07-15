# ejemplo de negacion not - invertir la logica de programacion
print('*** Bienvenido al Sistema Bancario ***')

salir_sistema_txt = input('Desea salir del Sistema? (Si/No): ')
salir_sistema = salir_sistema_txt.strip().lower() == 'si'

if not salir_sistema:
    print('Continuamos dentro del Sistema')
else:
    print('salimos del sistema')