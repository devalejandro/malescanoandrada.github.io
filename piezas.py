from mimetypes import init


class pieza():
    def __init__(self, color, posx, posy):
        self.color = color
        self.posx = posx
        self.posy = posy
        self.mov = False
        print("Se ha credo la pieza")
    
    def posicion(self):
        return f"Posición X: {self.posx}, Posicion Y: {self.posy}"

class peon(pieza):
    def __init__(self, color, posx, posy):
        pieza.__init__(self, color, posx, posy)
    
    def mover(self):
        if self.mov == False:
            paso = 3
            while(int(paso) > 2 or int(paso) < 0):
                paso = int(input("Ingrese 1 o 2: "))
            self.posy = self.posy + paso
            self.mov = True
        else:
            self.posy = self.posy + 1
        return self.posy

class torre(pieza):
    def __init__(self, color, posx, posy):
        pieza.__init__(self, color, posx, posy)
    
    def mover(self):
        direccion = input("En que dirección se mueve? x/y: ")
        casillas = int(input("Cantidad de casillas: "))

        if(direccion == "x"):
            sentido = input("Sentido derecha/izquierda: ")
            if(sentido == "derecha"):
                self.posx = self.posx + casillas
            else:
                self.posx = self.posx - casillas
        else:
            sentido = input("Sentido arriba/abajo: ")
            if(sentido == "arriba"):
                self.posy = self.posy - casillas
            else:
                self.posy = self.posy + casillas

peon1 = peon("Negro",2,2)
torre1 = torre("Negro",1,1)
print(torre1.posicion())
torre1.mover()
print(torre1.posicion())
print(peon1.posicion())
peon1.mover()
print(peon1.posicion())