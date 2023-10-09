class Animal:
    def __init__(self, especie, edad) -> None:
        self.especie = especie
        self.edad = edad
    
    def hablar(self):
        pass
    
    def caminar(self):
        pass
    
    def describeme(self):
        print("Soy un animal del tipo", type(self).__name__)
    
class perro(Animal):
    def __init__(self, especie, edad, dueño) -> None:
        super().__init__(especie, edad)
        self.dueño = dueño
    
    def hablar(self):
        print("guau guau")
        
    def caminar(self):
        print("camina en cuatro patas")
    
class Vaca(Animal):
    def hablar(self):
        print("Muu")
    def caminar(self):
        print("caminando en cuatro patas")

class Abeja(Animal):
    def hablar(self):
        print("bzzzz")
    def caminar(self):
        print("Vuela")
    def picar(self):
        print("Esta picando!")
    

mi_perro = perro("mamifero", 5, "Luis")
print(mi_perro.especie)
print(mi_perro.edad)
print(mi_perro.dueño)