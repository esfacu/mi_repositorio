class Clase1:
    ...
class Clase2:
    ...
class Clase3:
    ...
    
class Clase4(Clase1, Clase3, Clase2)
    ...

print(Clase4.__mro__)