#funcion registro al invocarse solicita mediante input usuario y pass

def registro(DB):
    while True:
        usuario = input("Ingrese el nombre de usuario a registrar (o 'q' para salir): ")
        if usuario == 'q':
            break

        contraseña = input("Ingrese la contraseña a registrar: ")
        DB[usuario] = contraseña
        print("Registro exitoso")


# funcion de guartdado, almacena en una database usuario y contraseña en un archivo de txt. Si el archivo no existe, se creaa
def guardarDB(DB):
    with open("database.txt", "w") as archivo:
        for usuario, contraseña in DB.items():
            archivo.write(f"{usuario}:{contraseña}\n")
    print("Base de datos guardada correctamente. Programa finalizado!")


# cargar db desde database.txt y devuelve como diccionario incluye un except si no encuentra el txt inicia db como un diccionario vacio
def cargarDB():
    try:
        with open("database.txt", "r") as archivo:
            DB = {}
            for linea in archivo:
                usuario, contraseña = linea.strip().split(":")
                DB[usuario] = contraseña
    except FileNotFoundError:
        DB = {}
    return DB

# imprime DB por pantalla
def leerData(DB):
    print("La Base de datos contiene los siguientes elementos: ")
    for usuario, contraseña in DB.items():
        print(f"Usuario: {usuario}, Contraseña: {contraseña}")

# opciones de login, se agrega "q" como metodo de escape
def login(DB):
    while True:
        usuario = input("Ingrese su nombre de usuario (o 'q' para salir): ")
        if usuario == 'q':
            break
        contraseña = input("Ingrese su contraseña: ")

        if usuario in DB:
            if DB[usuario] == contraseña:
                print("Ingreso exitoso")
            else:
                print("Contraseña incorrecta")
        else:
            print("Usuario no encontrado")

DB = cargarDB()

# Se emplea while para simular interfaz usuario, mediante un bucle infinito que se ejecuta hasta que se utiliza la opción 4 "guardar y salir"
while True:
    print("\n1. Registro")
    print("2. Leer datos")
    print("3. Login")
    print("4. Guardar y salir")

# 1 llama a registro() // 2 llama leerDatos() para mostrar por pantalla // 3 invoca login // 4 guarda la base de datos en archivo y luego usa break para salir del bucle // el else contempla que usuario ingrese una distinta a las ofrecidas
    opcion = input("Elija una opción: ")
    if opcion == '1':
        registro(DB)
    elif opcion == '2':
        leerData(DB)
    elif opcion == '3':
        login(DB)
    elif opcion == '4':
        guardarDB(DB)
        break
    else:
        print("Opción no válida, por favor ingrese una opción válida.")


