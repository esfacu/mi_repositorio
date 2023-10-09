import sys
sys.path.append("..")  # Agrega la ruta al directorio principal del proyecto, para poder volver atras con .. y buscar el otro modulo
#importo del otro modulo la clase Alumno
from moduloClase.clase import Alumno

#instancio mi alumno como alumno1 e imprimo sus datos
alumno1 = Alumno("Facundo", 10)
print(alumno1)
