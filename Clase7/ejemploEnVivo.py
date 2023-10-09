class Televisor:
    colores = {"Blanco", "Negro", "Rojo", "Azul", "Gris"}
    letras_costo = {"A": 100, "B": 80, "C": 60, "D": 50, "E": 30, "F": 10}

    def __init__(self, precio_base=100, color="blanco", consumo_energetico="F", peso=5):
        self.comprobar_color(color)
        self.comprobar_consumo(consumo_energetico)
        self.precio_base = precio_base  # Corregido
        self.peso = peso  # Corregido

    def comprobar_color(self, color):
        color = color.lower()
        if color in self.colores:
            self.color = color
        else:
            self.color = "blanco"

    def comprobar_consumo(self, consumo_energetico):
        if consumo_energetico in self.letras_costo:
            self.consumo_energetico = consumo_energetico
        else:
            self.consumo_energetico = "F"

    def precio_final(self):
        precio = self.precio_base
        if self.peso >= 0 and self.peso <= 19:
            precio += 10
        elif self.peso >= 20 and self.peso <= 49:
            precio += 50
        elif self.peso >= 50 and self.peso <= 79:
            precio += 100

        precio += self.letras_costo[self.consumo_energetico]
        return precio


televisores = [Televisor(250, "rojo", "E", 10)]  # Corregido

def total(televisores):
    total_precio = 0
    for t in televisores:
        total_precio += t.precio_final()
    return total_precio

print(total(televisores))
