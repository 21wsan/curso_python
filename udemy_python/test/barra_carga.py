# barra de carga en Python

import time
import sys

print('\n**** Probando barra de carga en Python ****\n')

# pasos
total = 20

for i in range(total +1):
    porcentaje = int((i / total) * 100)
    barra = '#' * i + '-' * (total - i)
    sys.stdout.write(f'\rCargando: |{barra}| {porcentaje}%')
    sys.stdout.flush()
    time.sleep(0.2) # simula el tiempo
print('\n¡Carga completada!')