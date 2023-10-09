import os

def crear_tabla(numero):
    contenido = ""
    for i in range(1, 11):
        resultado = numero * i
        contenido += f"{numero} x {i} = {resultado}\n"

    nombre_archivo = f"tabla-{numero}.txt"
    ruta_archivo = os.path.abspath(nombre_archivo)  # Obtener la ruta completa del archivo
    with open(nombre_archivo, "w") as archivo:
        archivo.write(contenido)

    print(f"Se creó la tabla y se guardó en: {ruta_archivo}")

def mostrar_tabla(numero, linea):
    nombre_archivo = f"tabla-{numero}.txt"
    try:
        with open(nombre_archivo, "r") as archivo:
            lineas = archivo.readlines()
            if len(lineas) >= linea:
                print(f"Tabla de número {numero}, línea {linea}:\n{lineas[linea - 1]}")
            else:
                print("La línea especificada no existe en el archivo.")
    except FileNotFoundError:
        print("No existe la tabla")

def mostrar_menu():
    print("1- Generar tabla")
    print("2- Mostrar tabla")
    print("3- Salir")

def validar_opcion(opcion):
    return opcion in ["1", "2", "3"]

def main():
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if validar_opcion(opcion):
            if opcion == "1":
                numero = int(input("Ingrese un número entero: "))
                crear_tabla(numero)
            elif opcion == "2":
                numero = int(input("Ingrese un número entero: "))
                linea = int(input("Ingrese el número de línea que desea mostrar: "))
                mostrar_tabla(numero, linea)
            else:
                print("Hasta luego")
                break
        else:
            print("Error: opción incorrecta")

if __name__ == "__main__":
    main()
