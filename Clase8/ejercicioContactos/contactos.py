import json

def agregar_contacto():
    nombre = input("Ingrese el nombre: ")
    apellido = input("Ingrese el apellido: ")
    telefono = input("Ingrese el teléfono: ")
    direccion = input("Ingrese la dirección: ")
    
    contacto = {
        "nombre": nombre,
        "apellido": apellido,
        "telefono": telefono,
        "direccion": direccion
    }

    # Cargar contactos existentes o inicializar una lista si el archivo no existe
    try:
        with open("contactos.json", "r") as archivo:
            contactos = json.load(archivo)
    except FileNotFoundError:
        contactos = []

    # Agregar el nuevo contacto
    contactos.append(contacto)

    # Guardar la lista de contactos en el archivo json
    with open("contactos.json", "w") as archivo:
        json.dump(contactos, archivo)

    print("Contacto agregado correctamente.")

def ver_informacion():
    nombre = input("Ingrese el nombre: ")
    apellido = input("Ingrese el apellido: ")

    # Cargar contactos existentes o mostrar un mensaje si el archivo no existe
    try:
        with open("contactos.json", "r") as archivo:
            contactos = json.load(archivo)
    except FileNotFoundError:
        print("No hay contactos almacenados.")
        return

    encontrado = False
    # Buscar el contacto por nombre y apellido
    for contacto in contactos:
        if contacto["nombre"] == nombre and contacto["apellido"] == apellido:
            print("Información del contacto:")
            print(f"Nombre: {contacto['nombre']}")
            print(f"Apellido: {contacto['apellido']}")
            print(f"Teléfono: {contacto['telefono']}")
            print(f"Dirección: {contacto['direccion']}")
            encontrado = True
            break

    if not encontrado:
        print("Contacto no encontrado.")

def mostrar_menu():
    print("1- Agendar contacto")
    print("2- Ver información de contacto")
    print("3- Salir")

def main():
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            agregar_contacto()
        elif opcion == "2":
            ver_informacion()
        elif opcion == "3":
            print("Hasta luego.")
            break
        else:
            print("Opción inválida. Por favor, seleccione una opción válida.")

if __name__ == "__main__":
    main()
