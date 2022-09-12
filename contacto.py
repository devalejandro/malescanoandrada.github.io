class Contacto:
    def __init__(self, nombre, apellido, edad, direccion):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.direccion = direccion
    
    def mostrarContacto(self):
        print(f"Nombre: {self.nombre}\nApellido: {self.apellido}\nEdad: {self.edad}\nDireccion: {self.direccion}")
    
nuevo_contacto = Contacto("Alejandro","Lescano", 26, "Ceipos 2")
nuevo_contacto2 = Contacto("Agustin","Lescano", 24, "Yacampis")
nuevo_contacto.mostrarContacto()
nuevo_contacto2.mostrarContacto()
