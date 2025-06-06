import math

# trunc() = elimina los decimales de un numero float

a=123.56
b=math.trunc(a)
print("el valor truncado es",b)

# fabs() = calcula el valor absoluto de un numero float, eliminando el signo
a = -200.45
b = math.fabs(a)
print("el valor absoluto es",b)

# factorial() = calcula el numero de combinaciones posibles de una serie de objetos, solo con numeros enteros
# se expresa como n! ej: 0! ==

a = 6
b = math.factorial(a)
print("el valor factorial de",a,"es:",b)

# fmod() = calcula el residuo de una division entre dos numeros float
c=math.fmod(16,5)
print("el residuo de dividir 16 entre 5 es:",c)

# sqrt() = calcula la raiz cuadrada de un numero entero
a=3
b=math.sqrt(a)
print("la raiz cuadrada de 3 es:",b)

# Las funciones trigonométricas seno, coseno y tangente se realizan usando sin(), cos() y tan().
'''
Las funciones trigonométricas en la librería math toman los valores de los ángulos expresados como radianes. 
Por esta razón, debe realizarse la conversión de grados a radianes con la función radians.
'''

angulo=60
radianes=math.radians(angulo)
print("los radianes son:",radianes)

seno=math.sin(radianes)
coseno=math.cos(radianes)
tangente=math.tan(radianes)

print("el seno es:",seno)
print("el coseno es:",coseno)
print("la tangente es:",tangente)