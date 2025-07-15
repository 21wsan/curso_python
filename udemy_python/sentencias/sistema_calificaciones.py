print('*** Sistema de Calificaciones ***')

nota = float(input('Digite la calificación final entre 0 y 10: '))
nota_final = None

if 9 <= nota <= 10:
    nota_final = 'A'
elif 8 <= nota < 9:
    nota_final = 'B'
elif 7 <= nota < 8:
    nota_final = 'C'
elif 6 <= nota < 7:
    nota_final = 'D'
elif 0 <= nota < 6:
    nota_final = 'F'
else:
    print('Valor desconocido')

# imprimir datos
print(f'La nota {nota} es equivalente a: {nota_final}')
