print('*** Valor Dentro del Rango ***')

VALOR_MINIMO = 0
VALOR_MAXIMO = 5

valor_usuario = int((input(f'ingrese un valor entre {VALOR_MINIMO} y {VALOR_MAXIMO}: ')))

# dentro_rango = valor_usuario >= VALOR_MINIMO and valor_usuario <= VALOR_MAXIMO
dentro_rango = VALOR_MINIMO <= valor_usuario <= VALOR_MAXIMO
print(f'el valor esta dentro de rango?: {dentro_rango}')