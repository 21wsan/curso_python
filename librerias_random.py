import random

# genera un numero aleatorio entre los valores indicados(valor1, valor2)
a = random.randint(10,100)
print(a)

# genera un numero entero aleatorio entre 0 y 100 incrementos de 5
b= random.randrange(0,100,5)
print(b)

# genera un numero float aleatorio entre 0.0 y 1.0
c=random.random()
print(c)

# genera un numero float aleatorio entre 100.0 y 200.0 inclusive
d=random.uniform(100,200)
print(d)

# funcion choice permite seleccionar al azar un dato dentro de un conjunto
jugador=["Jhon","Luis","Juan","Maria","Patricia"]
ganador=random.choice(jugador)
print("el ganador es",ganador)

# la funcion shuffle() = modifica el orden de los elementos en una lista
cartas=[1,2,3,4,5,6,7,8,16,14,15,17]
random.shuffle(cartas)
print(cartas)

# sample() = esta funcion extrae una cantidad de numeros aleatorios de un conjunto
naipes=[9,8,7,6,5,4,2,1]
print(random.sample(naipes,3))
