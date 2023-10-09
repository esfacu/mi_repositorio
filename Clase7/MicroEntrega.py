class auto():
   def __init__(self, modelo, marca):
        #Atributos de instancia
        self.modelo = modelo
        self.marca = marca

      
miAuto = auto("gol", "VW")
auto2 = auto("Toyota", "Corolla")

print(f"Marca: {miAuto.marca}")
print(f"Modelo: {miAuto.modelo}")

print(f"El auto 2 es de la marca {auto2.marca} y tiene el modelo {auto2.modelo}")
