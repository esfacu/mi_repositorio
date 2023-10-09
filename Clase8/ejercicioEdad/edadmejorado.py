from datetime import datetime

# Obtiene la fecha y hora actual
fecha_actual = datetime.now()

# Obtiene la fecha de nacimiento
fecha_nacimiento = datetime(1994, 12, 3)

# Calcula la edad
edad = fecha_actual.year - fecha_nacimiento.year - ((fecha_actual.month, fecha_actual.day) < (fecha_nacimiento.month, fecha_nacimiento.day))

# Imprime la fecha actual y la edad
print(f"La fecha actual es: {fecha_actual.day}/{fecha_actual.month}/{fecha_actual.year}")
print(f"Tu edad es {edad} años.")
