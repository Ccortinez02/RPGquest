class Habilidad:
    def __init__(self, nombre, costo_mana, daño, efecto):
        self.nombre = nombre
        self.costo_mana = costo_mana
        self.daño = daño
        self.efecto = efecto

    def __str__(self):
        return f"{self.nombre}: Costo de maná: {self.costo_mana}, Daño: {self.daño}, Efecto: {self.efecto}"
