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
    print("Que putas quiere hacer?\n 1 - Sumar\n 2 - Restar\n 3 - Multiplicar\n 4 - Dividir\n")

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

operar()