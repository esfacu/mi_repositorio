# Abre el archivo en modo escritura
f = open("miHobbieFavorito.txt", "w")

# Lista para almacenar los hobbies
hobbies = []

# Solicita tres hobbies al usuario y los escribe en el archivo
for i in range(3):
    hobbie = input(f"Ingrese su Hobbie #{i + 1}: ")
    hobbies.append(hobbie)  # Agrega el hobbie a la lista
    f.write(f"{hobbie}\n")  # Escribe el hobbie en el archivo

# Cierra el archivo antes de leerlo
f.close()

# Abre el archivo en modo lectura
f = open("miHobbieFavorito.txt", "r")

# Lee y muestra el contenido del archivo
print("Contenido del archivo:")
print(f.read())

# Cierra el archivo después de leerlo
f.close()
