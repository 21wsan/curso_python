print('**** Regresar una tupla de valores desde una función ****')

# Definicion de la funcion
def persona_mayusculas(nombre, apellido, edad):
    print('esta funcion regresa varios valores (tupla)')
    return (nombre.upper(), apellido.upper(), edad)   # esto regresa una tupla, es opcional el parentesis pero al separar por (,) sabemos que es una tupla

# programa principal
nombre, apellido, edad = persona_mayusculas('Alejandra', 'Jimenez', 32)
print(f'resultado persona = Nombre: {nombre} Apellido: {apellido} Edad: {edad}')