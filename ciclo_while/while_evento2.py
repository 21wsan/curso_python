print("uso del ciclo while + else")

promedio, total, contador=0,0,0

print("==== Softwate para Parking ====")
placa=input("introduzca la placa del vehiculo (99 para salir): ")
while placa != "99":
    valor = float(input("digite el valor del parqueo: "))
    total=total+valor
    contador=contador+1
    placa=input("introduzca la placa del vehiculo (99 para salir): ")
else:
    promedio=round(total / contador)
    print("Promedio del Vr del parqueadero por vehiculo: " + str(promedio))
    print("total de dinero recaudado: ",round(total))
    print("fin del ciclo while")
print("final del ciclo while + else")