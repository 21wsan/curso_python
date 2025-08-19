print('**** Argumentos Variables ****')

def superheroe_superpoderes(superheroe, nombre, *args): # *args siempre debe ir al final
    print(f'Superheroe: {superheroe} - {nombre} - {args}') # se define args sin el *
    # iteramos los superpoderes
    for superpoder in args:
        print(f'superpoder: {superpoder}')

# llamar la funcion
superheroe_superpoderes('spiderman', 'peter parker', 'Instinto aracnido', 'telaraña')
superheroe_superpoderes('iron man','tony stark', 'armadura', 'playboy','millonario')

# es opcional enviar argumentos variables
superheroe_superpoderes('mi vecino', 'jhon doe')