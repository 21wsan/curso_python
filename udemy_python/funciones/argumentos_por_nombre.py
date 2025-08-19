print("*** Funcion con argumentos por nombre ***")

def imprimir_persona(nombre, apellido='', edad=0):
    print(f'Persona: Nombre: {nombre} Apellido: {apellido} Edad: {edad}')

# llamamos la funcion pasando los argumentos de forma posicional
imprimir_persona('Sofia', 'Sandoval', 28)

# llamar la funcion usando argumentos por nombre
imprimir_persona(nombre='Vanessa', apellido='Camacho', edad=25)

# llamar la funcion usando argumentos por nombre intercambiando el orden
imprimir_persona(edad=25, apellido='Riaño', nombre='Liseth')

# argumentos con valor por default
imprimir_persona(nombre='Sandra')
# en la declaración de variables dentro de la funcion dejamos el apellido como cadena vacia y la edad en cero