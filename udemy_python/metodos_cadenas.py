# metodos de cadenas

cadena1 = "Hola Mundo"

print(f"cadena original: {cadena1}")
mayusculas = cadena1.upper()
print(f"cadena en mayusculas: {mayusculas}") # convertir a mayusculas
print(f"cadena en minusculas: {cadena1.lower()}") # convertir a minusculas

cadena2 = " Jhon Doe "
print(f"cadena con espacios: {cadena2}")
print(f"cadena sin espacios: {cadena2.strip()}") # elimina espacios al inicio y al final

# para obtener el largo de una cadena
cadena3 = "Hello my friend"
largo_cadena = len(cadena3)
print(f"el largo de la cadena es: {largo_cadena}")