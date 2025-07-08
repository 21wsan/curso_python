print('*** Calcular el área y perimetro de un rectangulo ***')

# pedir datos al usuario
base = float(input('Ingrese la base del rectangulo: '))
altura = float(input('Ingrese la altura del rectangulo: '))

# realizar los calculos
area = base * altura
perimetro = 2 * (base + altura)

print(f'el área del rectangulo es: {area:.2f}')
print(f'el perimetro del rectangulo es: {perimetro:.2f}')