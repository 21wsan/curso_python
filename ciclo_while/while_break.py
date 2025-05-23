print("uso de la sentencia BREAK en while")

variable=35

while variable > 1:
    variable = variable -5
    if variable == 10:
        break
    print("valor actual del caracter: " + str(variable))
print("fin del ciclo...")