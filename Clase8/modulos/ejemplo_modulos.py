
### NANEDTUPLE !!!! 
## Modulo namedtuple, crear clases facilmente con este modulo
# from collections import namedtuple

# pez = namedtuple("Pez", ["nombre", "especie", "peso"])
# pez1 = pez("Juan", "Pez espada", 1)
# nemo = pez("Nemo", "Payaso", 1)

# print(pez1, nemo)


### COUNTER !!!!!
# # # Counter modulo para contar cantidad  de cada item por ejemplo en este caso detecta esta el 1 cuantro veces
# from collections import Counter
# # lista = [1,2,3,4,5,6,7,8,9,1,1,1,2,2]
# # print(Counter(lista))

# # Podemos usarlo para contar estudiantes, si quiero cuente por estudiante hago split de espacios vacios,  en caso de no hacerlo cuenta las repeticiones de los caracteres 
# estudiantes = "Nicolas Claudia Facundo Brenda Flor Nicolas Flor Facundo Carlos"
# print(Counter(estudiantes.split(" "))) 
# print(Counter(estudiantes)) 


#datetime es un modulo para trabajar con la fecha
from datetime import datetime , timedelta

#dt now() nos trae la fecha actual a la cual la asigno a variables para luego printearla con mi formato 
dt = datetime.now()
dia = dt.day
mes = dt.month
anio = dt.year

# print(anio)
# print(mes)
# print(dia)
# print(f"La fecha actual es: {dia}/{mes}/{anio}")

# # con datetime segun documentacion puedo pasarle los datos que quiera incluya como atributus
# dt_prueba = datetime(2000, 1, 1)
# print(dt_prueba.year)
# print(dt_prueba.month)
# print(dt_prueba.day)

# # puedo pasar a cambiarlos posteriormente con el metodo replace()
# dt_prueba = dt_prueba.replace(2020)
# print(dt_prueba.year)
# print(dt_prueba.month)
# print(dt_prueba.day)

# # # PERSONALIZAR DATA TIME!!!!
# %A: Dia de la semana
# %d: Dia del mes
# %B: Nombre del mes
# %Y: Año
# %I: Hora
# %M: Minutos
# print(dt.strftime("%A %d %B %Y %I %M"))

#con time delta puedo jugar con fechas futuras o pasadas, con estos parametros avanza 14 dias, 4 horas y 1000 seg, si pusiera -14 nos muestra dos semanas en el pasado
# t = timedelta(days=14, hours = 4, seconds= 1000)
# dt_dentro_de_dos_semanas = dt + t
# print(dt_dentro_de_dos_semanas ,  dt)

# # # MODULO CALCULOS MATEMATICOS
# import math
# # # Raiz cuadrada
# # x = math.sqrt(64)
# # print(f"La raiz cuadrada de nuestro numero es: {x}")

# #REDONDEO AL ENTERO MAS CERCANO
# x = math.ceil(1.4)
# y = math.floor(1.4)

# print(f"Primero redondeo {x}") #ceil redondea para arriba sin importar el decimal que siga
# print(f"Primero redondeo {y}") #floor redondea para abajo sin importar el decimal que siga

#random devuelve numero random
import random
#step hace que vaya de 2 en 2, de esta manera salteamos los numeros impares
print(random.randrange(0,20, step=2))


#Uso de random en listas y string
lista = [1,2,"coder", -1, "Nico"]
string = " Esta es una cadena de caracteres."
print("Este es un random tomado de esta lista:  ", random.choice(lista))
print("Este es un random tomado de esta string:  ", random.choice(string))
#Le agregamos split para dividir por palabras
print("Este es un random tomado de esta string agregandole split:  ", random.choice(string.split()))





