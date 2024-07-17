from personaje import Personaje

class Jugador(Personaje):
    def __init__(self, nombre):
        super().__init__(nombre)
        self.inventario = []

    def mostrar_inventario(self):
        if not self.inventario:
            print("Tu inventario está vacío.")
        else:
            for item in self.inventario:
                print(item)
    def equipar_equipo(self):
        # Implementar la lógica para equipar equipo
        pass

    def usar_habilidad(self):
        # Implementar la lógica para usar habilidades
        pass
