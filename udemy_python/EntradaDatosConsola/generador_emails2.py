print('**** Sistema Generador de Emails ****')

name = input('Ingrese el nombre: ')
last_name = input('Ingrese el apellido: ')
company_name = input('Ingrese el nombre de la empresa: ')
ext_domain = input('Ingrese la extencion del dominio: ')

# normalizar valores
name_2 = name.strip().lower().replace(' ', '.')
last_name_2 = last_name.strip().lower().replace(' ', '.')
company = company_name.strip().lower().replace(' ', '')
domain = ext_domain.strip().lower().replace(' ', '')

email = (f'{name_2}.{last_name_2}@{company}{domain}')

# imprimir resultado
print(f'''
    Hola {name} {last_name} su nuevo Email generado por el sistema es:
      {email}
      gracias...
''')