# el programa solicita un número al usuario una y otra vez hasta que el usuario acierte.
import random

i=1

numero1=random.randrange(1,10)
numero2=int(input("digite un numero del 1 al 10: "))

while numero2 != numero1:
    i+=1
    numero2=int(input("digite un numero del 1 al 10: "))
print(f"<<<El numero secreto es {numero1} Acertaste en el intento numero: ",i,">>>")