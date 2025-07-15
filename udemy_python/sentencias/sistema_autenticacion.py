print('*** Sistema de Autenticación ***')

USER = 'root'
PASSWORD = '123'

usuario = input('Digite el nombre de usuario: ')
password = input('Digite la contraseña: ')

if usuario == USER and password == PASSWORD:
    print(f'Bienvenido al Sistema usuario {usuario}')
elif usuario == USER:
    print('Password incorrecto')
elif password == PASSWORD:
    print('Usuario incorrecto')
else:
    print('Usuario y Password incorrecto')