# import modulo_funcion_sumar
# importa la funcion sumar
from modulo_funcion_sumar import sumar

print('*** Funcion Sumar ***')

# Definir la funcion
'''
def sumar(a, b):
    resultado_suma = a + b
    return resultado_suma
'''
# llamar a la funcion sumar
if __name__ == '__main__':
    resultado_funcion = sumar(8, 5)
    print(f'Resultado de la funcion sumar: {resultado_funcion}')

    resultado_funcion = sumar(9, 15)
    print(f'Resultado de la funcion sumar: {resultado_funcion}')