# Generador de emails

print("**** Generador de Emails ****")
nombre_completo = ' Jhon Doe Rag '
print(f"Nombre Usuario: {nombre_completo}")
# procesar o normalizar el nombre de usaurio
# limpiar espacios al inicio y final
nombre_usuario = nombre_completo.strip()
# reemplazar los espacios en blanco por puntos
nombre_usuario = nombre_usuario.replace(' ', '.')
# convertir todo a minusculas
nombre_usuario = nombre_usuario.lower()
print(f"Nombre de Usuario Normalizado: {nombre_usuario}")

# Datos de la empresa
nombre_empresa = ' Global Mentoring '
print(f"\nNombre Empresa: {nombre_empresa}")
dominio = '.com.co'
print(f"Extencion del Dominio: {dominio}")
# quitar espacios en blanco y convertir en mayusculas
nombre_empresa = nombre_empresa.replace(' ', '').lower()
print(f"Dominio del Email Normalizado: {nombre_empresa}{dominio}")
# creamos el email final
email = f'{nombre_usuario}@{nombre_empresa}{dominio}'
print(f"\nEmail final generado: {email}")