# conversion de tipos de datos Python

# convertir de cadena a numero
numero_cadena = '10'
numero_entero = int(numero_cadena)
print(f"valor en cadena: {numero_cadena}")
print(f"cadena en numero entero: {numero_entero}")

# convertir de cadena a flotante
numero_cadena = '3.14'
numero_flotante = float(numero_cadena)
print(F"de cadena a flotante: {numero_flotante}")

# convertir de numero a cadena
numero_entero = 25
numero_cadena = str(numero_entero)
print(f"de numero entero a cadena: {numero_cadena}")

# convertir a booleano
# tipo bool es falso en los siguientes casos
# si el valor es 0, cadena vacía o None, entonces regresa False
# regresa True si los valores son distintos

numero_entero = 0
booleano = bool(numero_entero)
print(f"el booleano es: {booleano}")

numero_entero = 5
booleano = bool(numero_entero)
print(f"el booleano es: {booleano}")

cadena = '' # el largo de la cadena es 0
booleano = bool(cadena)
print(f"el valor de la cadena vacía es: {booleano}") # False, incluye colecciones vacias

cadena = 'cadena con valor'
booleano = bool(cadena)
print(f"valor booleano de cadena No Vacía: {booleano}")

variable = None
booleano = bool(variable)
print(f"el valor de la variable None es: {booleano}") # False