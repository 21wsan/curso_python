print('*** Sistema de Autenticación ***')

USUARIO = 'admin'
PASSWORD = '123'

usuario = (input('Cual es tu Usuario?: '))
password = (input('Cual es tu Password?: '))

validar = usuario.strip() == USUARIO and password.strip() == PASSWORD
print(f'Datos correctos?: {validar}')