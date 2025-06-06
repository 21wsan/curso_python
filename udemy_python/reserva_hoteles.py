print("*** Sistema de Reserva de Hoteles ***")
print()
print("<<< realizar reserva >>>")

nombre_cliente=input("Ingrese el nombre del cliente: ")
dias_estancia=int(input("Ingrese los días de Instancia: "))
tarifa_diaria=None
vista_al_mar=input("con vista al mar: ")

if vista_al_mar == "si":
    tarifa_diaria=1200.0
if vista_al_mar == "no":
    tarifa_diaria=1000.0

total=(tarifa_diaria*dias_estancia)

print()
# Mostrar detalle de la reserva
print(f"Cliente: {nombre_cliente}")
print(f"Días de estancia: {dias_estancia}")
print(f"Tarifa Diaria: {tarifa_diaria}")
print(f"Habitación con Vista al Mar?: {vista_al_mar}")
print(f"Valor total: {total}")

print(type(vista_al_mar))