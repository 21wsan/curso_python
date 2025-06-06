# TALLER 3 PYTHON
# AUTOR: WILLINTONG SANCHEZ NIETO
# FECHA: 16/05/2025

from datetime import date
# fecha actual
hoy=date.today()
print("hoy es el día: ",hoy)

a=int(input("digite el valor de A: "))
b=int(input("digite el valor de B: "))
if a>=b:
    print("A es mayor o igual que B")
else:
    print("A es menor que B")
print()
curso1="Requerimientos"
curso2="Algoritmos"
print("El curso1 es: ", curso1)
print("El curso2 es: ", curso2)

if curso1 == "Requerimientos" and curso2 == "Algoritmos":
    print("usted estudia programacion de software")
else:
    print("usted estudia otro programa diferente a programacion de software")
print()
print("*** Final del Analisis del programa de formación SENA ***")
print()
frase=input("digite una oración: ")
print("La frase en mayuscula es: ",frase.upper())
longitud=len(frase)
print("La longitud de la frase es: ", len(frase), "caracteres")
if longitud > 10:
    print("La frase contiene mas de 10 caracteres...")
else:
    print("La frase contiene menos de 10 caracteres...")
print()
print("FIN")
