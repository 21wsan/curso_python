import math

print("*** Constantes en Python ***")

# se escriben en mayusculas separando las frases con un guion bajo _
PI = 3.14159
print(f"el valor de PI es: {PI}")

NOMBRE_BASE_DATOS = "Clientes_db"
print(f"nombre de la base de datos: {NOMBRE_BASE_DATOS}")

# no se debe cambiar el valor de una constante EJ:

NOMBRE_BASE_DATOS = "listado_clientes_db"
print(f"no cambiar el valor de un aconstante: {NOMBRE_BASE_DATOS}")

# usar un aconstante en python, aunque no esta en mayusculas (math.pi)
print(f"el valor de PI es: {math.pi}")

