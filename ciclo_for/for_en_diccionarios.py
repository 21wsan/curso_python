# imprime los datos del diccionario
ensalada={'Manzana':'Verde','Mango':'Amarillo','sandia':'rosado','Papaya':'naranja'}

for nombre, color in ensalada.items():
    print(nombre," es de color",color)
print("fin del ciclo for...")

# otra forma
print("<<< forma numero 2 >>>")
# esto es un diccionario
ensalada2={'Manzana':'Verde','Mango':'Amarillo','sandia':'rosado','Papaya':'naranja'}

for elemento in ensalada2:
    print(elemento,"es de color",ensalada2[elemento])