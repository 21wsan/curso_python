# uso de la instruccion continue en python
print("uso de la sentencia continue")
num = 15

while num > 1:
    num = num -2
    if num == 9:
        continue
    print("el valor actual de num es: " + str(num))
print("fin del ciclo...")