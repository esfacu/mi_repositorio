from datetime import datetime

# Solicita al usuario su fecha de nacimiento
dia_nacimiento = int(input("Ingresa el día de tu nacimiento: "))
mes_nacimiento = int(input("Ingresa el mes de tu nacimiento: "))
anio_nacimiento = int(input("Ingresa el año de tu nacimiento: "))

# Obtiene la fecha y hora actual
fecha_actual = datetime.now()

# Obtiene la fecha de nacimiento
fecha_nacimiento = datetime(anio_nacimiento, mes_nacimiento, dia_nacimiento)

# Calcula la edad
edad = fecha_actual.year - fecha_nacimiento.year - ((fecha_actual.month, fecha_actual.day) < (fecha_nacimiento.month, fecha_nacimiento.day))

# Calcula la fecha del próximo cumpleaños para el año actual
fecha_cumpleanos = datetime(fecha_actual.year, fecha_nacimiento.month, fecha_nacimiento.day)

# Si el cumpleaños ya pasó este año, calcula la fecha para el próximo año
if fecha_actual > fecha_cumpleanos:
    fecha_cumpleanos = datetime(fecha_actual.year + 1, fecha_nacimiento.month, fecha_nacimiento.day)

# Calcula la diferencia en tiempo hasta el próximo cumpleaños
diferencia = fecha_cumpleanos - fecha_actual
segundos_faltantes = diferencia.total_seconds()

print("Tu edad es:", edad, "años.")
print("Faltan", int(segundos_faltantes), "segundos para tu próximo cumpleaños")

