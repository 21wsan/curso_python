# *args - argumentos - tupla
# **kwargs - keyword arguments (key, value) como un diccionario
print('*** Argumentos en forma de diccionario ***')

def superheroe_superpoderes(nombre, *args, **kwargs):
    print(f'Superheroe: {nombre}, {args}, {kwargs}')

# llamada a funcion
superheroe_superpoderes('spiderman', 'instinto aracnido', edad=17, empresa='marvel')
superheroe_superpoderes('iron man', 'armadura', 'playboy', edad=45)

# es opcional enviar argumentos variables
superheroe_superpoderes('mi vecino')
superheroe_superpoderes('mi vecino', personalidad='buena onda!')