# Creando Clases de manera habitual
# class Alumno:
#     def __init__(self, nombre, edad):
#         self.nombre = nombre
#         self.edad = edad

#     def __str__(self):
#         return f"Nombre: {self.nombre}, Edad: {self.edad}"


#Creandola mediante el uso de namedtuple
from collections import namedtuple

Alumno = namedtuple("Alumno", ["nombre", "nota"])
#reciclamos codigo de namedtuple ejemplo clase


# # print(alumno1)