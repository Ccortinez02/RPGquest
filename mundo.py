class Mundo:
    def __init__(self, nombre):
        self.nombre = nombre
        self.extension = "100m"

    def explorar(self):
        print("Explorando el mundo " + self.nombre + " de " + str(self.extension))