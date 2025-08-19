print('**** Alcance de Variables ****')

# variable global, se usa en cualquier parte del codigo
contador_global = 0

def incrementar_contador():
    # definir una variable local, solo se usa dentro de la funcion
    contador_local = 0

    # usar la variable global
    global contador_global
    #incrementar la variable global
    contador_global += 1
    
    # incrementar la variable local
    contador_local += 1

    # imprimir ambos contadores
    print(f'Contador local = {contador_local}')
    print(f'Contador global = {contador_global}\n')

# llamar varias veces la funcion
incrementar_contador()
incrementar_contador()
incrementar_contador()

# valor final variable global
print(f'Valor contador global = {contador_global}')