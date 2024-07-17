class Equipo:
    def __init__(self, nombre, tipo, ataque, defensa):
        self.nombre = nombre
        self.tipo = tipo
        self.ataque = ataque
        self.defensa = defensa

    def __str__(self):
        return f"{self.nombre} ({self.tipo}): Ataque: {self.ataque}, Defensa: {self.defensa}"
