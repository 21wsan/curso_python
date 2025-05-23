num=int(input("ingrese un numero: "))
'''
range, se especifica un valor con el cual itera el for, si se especifica un valor inicial y uno final
se imprimira se imprimira desde el valor inicial hasta el final -1
'''
for i in range(1,11):
    print(num,"X",i,"=",(num*i))
print("fin del ciclo...")