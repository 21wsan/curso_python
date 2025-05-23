print("sentencia CONTINUE en while")

variable = 35

while variable > 1:
    variable = variable -5
    if variable == 15:
        continue
    print("Valor actual de la variable:", str(variable))
print("fin del ciclo")

