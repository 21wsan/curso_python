print('*** Funcion Range ***')

# uso de range, hasta el valor final sin incluirlo
for i in range (11):
    print(i, end = ' ') # end = ' ' imprime la línea en forma horizontal

print('\n')
# uso de range(inicio, fin, incremento)
for i in range(0,10,2):
    print(i, end = ' ')

print('\n\nSecuencia del 10 al 20')
# incremento = 1 (default y es opcional)
for i in range(10,20 + 1):
    print(i, end = ' ')


print('\n\nSecuencia del 20 al 30 de 2 en 2')
for i in range(20, 30 + 1, 2):
    print(i, end = ' ')