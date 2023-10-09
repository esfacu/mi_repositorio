# # Abre el archivo en modo escritura
# with open("miHobbieFavorito.txt", "w") as archivo:
#     # Bucle para solicitar los hobbies y escribirlos en el archivo
#     for i in range(3):
#         hobby = input(f"Ingrese su hobby favorito #{i + 1}: ")
#         # Escribe el hobby en el archivo
#         archivo.write(f"{hobby}\n")

# print("Hobbies guardados en miHobbieFavorito.txt")

try:
    # Solicita tus hobbies favoritos
    hobbies = []
    for i in range(3):
        hobby = input(f"Ingrese su hobby favorito #{i + 1}: ")
        hobbies.append(hobby)

    # Abre el archivo en modo escritura (o lo crea si no existe en la misma carpeta del script)
    with open("miHobbieFavorito.txt", "w") as archivo:
        # Escribe los hobbies en el archivo
        for hobby in hobbies:
            archivo.write(f"{hobby}\n")

    print("Hobbies guardados en miHobbieFavorito.txt")

except Exception as error:
    print(f"Error: {error}")
