#datetime es un modulo para trabajar con la fecha
from datetime import datetime

#dt now() nos trae la fecha actual a la cual la asigno a variables para luego printearla con mi formato 
dt = datetime.now()
dia = dt.day
mes = dt.month
anio = dt.year

print(anio)
print(mes)
print(dia)
print(f"La fecha actual es: {dia}/{mes}/{anio}")

# # con datetime segun documentacion puedo pasarle los datos que quiera incluya como atributus
dt_nacimiento = datetime(1994, 12, 3)
dianacimiento = dt_nacimiento.day
mesnacimiento = dt_nacimiento.month
anionacimiento = dt_nacimiento.year


edad = anio - anionacimiento
print(f"Tu edad es {edad}")



