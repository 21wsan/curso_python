# TALLER: Ciclo FOR
# AUTOR: Willintong Sanchez Nieto
# FECHA: 27/5/2025

from datetime import date

hoy = date.today()
print(f"hoy es el día {hoy}")
print()
print("TALLER CICLOS ITERATIVOS CON LA SENTENCIA FOR")
print()
num1=int(input("digite el primer numero: "))
num2=int(input("digite el segundo numero (mayor): "))
print("cliclo para el primer numero")
for i in range(num1):
    print(i)
print("fin del ciclo...")

print()
print("Ciclo Desde el Primer Numero Hasta el Segundo Numero")
for i in range(num1,num2):
    print(i)
print("fin del ciclo...")

print()
print("Ciclo Desde el Primer Numero Hasta el Segundo Numero con Incrementos de 2")
for i in range(num1, num2, 2):
    print(i)
print("fin del ciclo...")

print()
empresa = (input("digite el nombre de una empresa: "))
empresa = empresa.lower()
for caracter in empresa:
    print(caracter)
print("fin del ciclo...")

print()
print("FIN...")
