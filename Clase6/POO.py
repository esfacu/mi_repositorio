a = int(input("Inserta el número a: "))
b = int(input("Inserta el número b: "))

def dividir(a, b):
    try:
        resultado = a / b  # Intentamos realizar la división
        return resultado
    except ZeroDivisionError as z:
        print("Error: No puedes dividir por cero")
    except ValueError:
        print("Error: Debes ingresar números válidos")
    except Exception as e:
        print("Ha ocurrido un error:", type(e).__name__)
        return None  # También puedes devolver None para manejar otros casos de error

resultado = dividir(a, b)
if resultado is not None:
    print("Resultado de la división:", resultado)

