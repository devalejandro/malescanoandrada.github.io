#Definir un método que permita simular la tirada al azar de un dado de n caras
import random

class dado():
    def __init__(self, cantidad_caras): #Constructor
        self.cantidad_caras = cantidad_caras    #Atributo
    
    def tirada(self):
        #Se genera una variable que contiene un número random entre 1 y el número que se le pase al contructor.
        cara_mostrar = random.randint(1, self.cantidad_caras)
        return f"Salió: {cara_mostrar}"
    
    def cantidad_dados(self, cantidad):
        for i in range(cantidad):
            cont = i
            i = self.tirada()
            print(f"Para el dado {cont+1} salió {i}")

dado1 = dado(6)
dado2 = dado(50)
dado1.cantidad_dados(6)
dado2.cantidad_dados(2)