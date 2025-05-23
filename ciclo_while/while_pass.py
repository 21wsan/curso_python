# La sentencia Pass se utiliza cuando se requiere por sintaxis una instrucción pero
#  no se requiere ejecutar ningún comando o código.
print("sentencia PASS en while")

variable = 35

while variable > 1:
    variable = variable -5
    if variable == 25:
        pass
    print("Valor actual de la variable: ", str(variable))