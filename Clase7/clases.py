class Perro:
    
    especie = "Mamifero"
    
    #El constructor
    def __init__(self, nombre, raza):
        #Atributos de instancia
        self.nombre = nombre
        self.raza = raza
        
    def ladrar(self):
        print("Este perro acaba de ladrar!")

    def caminar(self, pasos):
        print("Este perro acaba de caminar {pasos}")
        

perro1 = Perro("Sammy", "Caniche")
#print(perro1.raza)
#print(perro1.nombre)
#print(perro1.especie)


print(perro1.ladrar())
print(perro1.caminar(10))