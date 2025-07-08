# Revisar si una variable se encuentra dentro del rango de 1 y 10
dato = int(input('Proporciona un Dato Entero: '))

# revisamos si esta dentro de rango
esta_dentro_de_rango = 1 <= dato <= 10
print(f'Variable esta dentro del rango (entre 1 y 10)? : {esta_dentro_de_rango}')

# Revisar logica inversa, si el dato esta fuera de rango
# esta_fuera_rango = not (1 <= dato <= 10)
# print(f'Variable esta fuera de rango?: {esta_fuera_rango}')