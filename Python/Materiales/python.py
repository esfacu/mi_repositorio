cadena = "acitametaM ,5.8 , otipeP ordeP"

# da vuelta la cadena
cadena_inversa = cadena[::-1]
print(cadena_inversa)

# Extrae nombre y apellido
nombre_apellido = cadena_inversa.split(',')[0]
print(nombre_apellido)

# Extrae nota
nota = cadena_inversa.split(',')[1]
print(nota)
# Extrae materia

materia = cadena_inversa.split(',')[2]
print(f"la materia es {materia}")
# Crear cadena formateada

texto_formateado = f"{nombre_apellido} ha sacado un {nota} en {materia}"
print(texto_formateado)


# print en pantalla
