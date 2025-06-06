def main():
    name = input("Ingrese su nombre: ")
    hello(name)
    hello()

def hello(to="world"):
    print("hello", to)

main()
