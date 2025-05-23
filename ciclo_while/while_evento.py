# Ciclo while controlado por evento

print("uso del ciclo while controlado por evento")

promedio, total, contador=0,0,0

print("==== Software para Parqueadero ====")
placa=input("introduzca la placa del vehiculo (99 para salir):")

while placa != "99":
    valor=float(input("Digite valor del parqueadero: "))
    total=total+valor
    contador=contador+1
    placa=input("introduzca la placa del vehiculo (99 para salir):")
promedio = round(total/contador)
print("Promedio de vr del parqueadero por vehiculo: " + str(promedio))
print("total dinero recaudado: ", round(total))
print("fin del ciclo while")