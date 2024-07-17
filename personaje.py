class Personaje:
    def __init__(self, nombre):
        self.nombre = nombre
        self.vida = 100
        self.ataque = 10
        self.defensa = 5
        self.habilidades = []
        self.poderes = []

    def atacar(self, objetivo):
        daño = self.ataque - objetivo.defensa
        if daño > 0:
            objetivo.vida -= daño
            print(f"{self.nombre} ataca a {objetivo.nombre} por {daño} puntos de daño.")
        else:
            print(f"El ataque de {self.nombre} no tiene efecto sobre {objetivo.nombre}.")

    def mostrar_estado(self):
        print(f"Ataque: {self.ataque}")
        print(f"{self.nombre}:")
        print(f"Vida: {self.vida}")
        print(f"Defensa: {self.defensa}")
        print(f"Habilidades: {', '.join([h.nombre for h in self.habilidades])}")
        print(f"Poderes: {', '.join([p.nombre for p in self.poderes])}")
