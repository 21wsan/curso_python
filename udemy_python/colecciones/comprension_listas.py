print('**** comprension de listas ****')

# una lista con el cuadrado de cada numero
numeros = [1,2,3,4,5,6]
cuadrados = [X**2 for X in numeros] # eleva al cuadrado cada elemento de la lista de numeros
print(cuadrados)

# lista de numeros pares
numeros = range(10+1)
pares = [X for X in numeros if X % 2 == 0]
print(pares)

# saludando a cada nombre
nombres = ['Ana', 'Sofia', 'Vanessa']
saludo = [f'hola {nombre}' for nombre in nombres]
print(saludo)