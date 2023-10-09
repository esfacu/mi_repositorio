class vehiculo():
    def tocar_bocina(self):
        print("Tocando bocina")
    def arrancar(self):
        print("arranco")
    def abrir_capot(self):
        print("se abre el capot")
        
        
class auto():
    def __init__(self, modelo, marca):
        #Atributos de instancia
        self.modelo = modelo
        self.marca = marca
    
class MovimientoEmbarcacion():
    def virar_a_estribor(self):
        print("girando estribor")
    def virar_a_babor(self):
        print("virando babor")

class lancha(vehiculo, MovimientoEmbarcacion):
    def __init__(self, nombreMotor):
        self.nombreMotor = nombreMotor
        
           
lancha = lancha("motorx")
lancha.virar_a_estribor()
lancha.abrir_capot()

