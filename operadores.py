class operadores:
    def __init__(self):
        self.a = 0
        self.b = 0
    
    def sumar(self):
        self.a = int(input("Ingresa el primer valor: "))
        self.b = int(input("Ingresa el segundo valor: "))
        print(f"El resultado es: {self.a + self.b}")
    
    def restar(self):

        self.a = int(input("Ingresa el primer valor: "))
        self.b = int(input("Ingresa el segundo valor: "))

        print(f"El resultado es: {self.a - self.b}")
    
    def multiplicar(self):
        self.a = int(input("Ingresa el primer valor: "))
        self.b = int(input("Ingresa el segundo valor: "))
        print(f"El resultado es: {self.a * self.b}")
    
    def dividir(self):
        self.a = int(input("Ingresa el primer valor: "))
        self.b = int(input("Ingresa el segundo valor: "))
        print(f"El resultado es: {self.a / self.b}")

def operar():
    print("\nQue quiere hacer?\n1 - Sumar\n2 - Restar\n3 - Multiplicar\n4 - Dividir\n")

    opcion = int(input("Ingresa una opción: "))

    operacion = operadores()

    if opcion == 1:
        operacion.sumar()
    elif opcion == 2:
        operacion.restar()
    elif opcion == 3:
        operacion.multiplicar()
    elif opcion == 4:
        operacion.dividir()
    else:
        print("Opción no valida.")

def menu():
    print("\n1 - Seleccionar una operación a realizar\n2 - Salir")

    opcion = int(input("Ingresa una opción: "))

    if(opcion == 1):
        operar()
    elif(opcion == 2):
        exit()
    else:
        print("Opción no válida.")

menu()