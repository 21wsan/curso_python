# Manejo de Subcadenas

cadena = "hola, mundo!"

# Obtenemos la subcadena de hola [inicio:fin (sin incluirlo)]
subcadena_hola = cadena[0:4]
print(f"subcadena de: {subcadena_hola}")

subcadena_mundo  = cadena[6:11]
print(f"subcadena de: {subcadena_mundo}")

# busqueda de subcadenas en python
cadena2 = "hola, mundo"
indice = cadena2.find("mundo")
print(f"indice de la subcadena mundo: {indice}")

#obtener el indice de la subcadena hola

indice = cadena2.find("hola")
print(f"indice de la subcadena hola: {indice}")
