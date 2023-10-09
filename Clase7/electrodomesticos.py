class Electrodomestico:
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


class Televisor(Electrodomestico):
    def __init__(self, precio_base=100, color="blanco", consumo_energetico="F", peso=5,
                 resolucion=20, sintonizador_tdt=False):
        super().__init__(precio_base, color, consumo_energetico, peso)
        self.resolucion = resolucion
        self.sintonizador_tdt = sintonizador_tdt

    def precio_final(self):
        precio = super().precio_final()
        if self.resolucion > 40:
            precio += precio * 0.30  # Correcto: Se incrementa un 30% si la resolución es mayor a 40 pulgadas
        if self.sintonizador_tdt:
            precio += 50  # Correcto: Se aumenta 50 si tiene sintonizador TDT
        return precio

class Lavadora(Electrodomestico):
    def __init__(self, precio_base=100, color="blanco", consumo_energetico="F", peso=5,
                 carga=5):
        super().__init__(precio_base, color, consumo_energetico, peso)
        self.carga = carga

    def precio_final(self):
        precio = super().precio_final()
        if self.carga > 30:
            precio += 50
        return precio
    
    

# Ejemplo de uso
mi_televisor = Televisor(precio_base=400, color="negro", consumo_energetico="F", peso=10,
                         resolucion=10, sintonizador_tdt=False)

print(f"Precio final del televisor: {mi_televisor.precio_final()}")


mi_lavadora = Lavadora(precio_base=300, color="blanco", consumo_energetico="B", peso=20, carga=35)
print(f"Precio final de la lavadora: {mi_lavadora.precio_final()}")