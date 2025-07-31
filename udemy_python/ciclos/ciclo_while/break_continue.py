print('*** Break y continue ***')

# ejemplo break
print('Palabra break')
for numero in range(1,10):
    if numero % 2 == 0:
        print(numero)
        break

# ejemplo continue
print('\nPalabra continue')
for numero in range(1,10):
    if numero % 2 == 1:
        continue
    print(numero)