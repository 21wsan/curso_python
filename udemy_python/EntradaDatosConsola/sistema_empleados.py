print("**** sistema empleados ****")

nombre_empleado = input("Nombre del Empleado: ")
edad_empleado = int(input('Edad del Empleado: '))
salario_empleado = float(input('Salario del Empleado: '))
es_jefe_departamento = input('Es Jefe Departamento (Si/No): ')

# convertir a tipo bool la variable es_jefe_departamento
es_jefe_departamento = es_jefe_departamento.lower() == 'si'

# imprimir valores del empleado
print('\n**** Datos del empleado ****')
print(f'Nombre: {nombre_empleado}')
print(f'Edad: {edad_empleado}')
print(f'Salario: {salario_empleado:.2f}')
print(f'Es Jefe de Departamento: {es_jefe_departamento}')