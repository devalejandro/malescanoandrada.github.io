# Generar un método que permita encriptar una palabra reemplazando vocales por números del 1 a 5.
class encriptador:
    def __init__(self, palabra):
        self.palabra = palabra

    def encriptar(self):
        palabra_lista = list(self.palabra) #En variable palabra_lista se guarda lo que se pase a self.palabra como una lista.

        repos_palabra_encriptada = [] #Guarda las letras analizadas y parseadas.

        for i in range(len(self.palabra)):  #Toma el largo de self.palabra y por cada iteración agrega la letra o el número a repos_palabra_encriptada.
            if palabra_lista[i].lower() == "a":
                repos_palabra_encriptada.append("1")
            elif palabra_lista[i].lower() == "e":
                repos_palabra_encriptada.append("2")
            elif palabra_lista[i].lower() == "i":
                repos_palabra_encriptada.append("3")
            elif palabra_lista[i].lower() == "o":
                repos_palabra_encriptada.append("4")
            elif palabra_lista[i].lower() == "u":
                repos_palabra_encriptada.append("5") #Si en la iteración la letra en el indice analizado es una vocal, se cambia por un número del 1 al 5.
            else:
                repos_palabra_encriptada.append(palabra_lista[i]) #Si en la iteración la letra no es una vocal la agrega tal y como está.

        palabra_encriptada = "".join(repos_palabra_encriptada) #Une los elementos de la lista repos_palabra_encriptada.
        
        print(palabra_encriptada) #Se imprime la palabra encripada.

textoSoloVocales = encriptador("aeiou")
textoContieneVocales = encriptador("MurCElago")
textoSoloVocales.encriptar()
textoContieneVocales.encriptar()