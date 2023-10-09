class Alumno():
    def __init__(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota

    def resultado(self):
        if self.nota < 5:
            return "El alumno desaprueba"
        elif self.nota >= 5:
            return "El alumno aprueba"
        else:
            return "Nota no válida"

    def imprimir(self):
        print(f"Nombre del alumno: {self.nombre} y  nota del alumno: {self.nota}")
        print(self.resultado())
        
        
        
#nombreAlumno = input("Ingrese nombre del alumno: ")
#notaAlumno = int(input("Ingrese nota del alumno: "))
#miAlumno = Alumno(nombreAlumno, notaAlumno)

#miAlumno.imprimir()


#creacion de instancias 
alumno1 = Alumno("Juan", 7)
alumno1.imprimir()
alumno2 = Alumno("Maria", 4)
alumno2.imprimir()
