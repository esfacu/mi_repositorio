#Type nos devuelve el tipo de dato, de esta manera podemos hacer que nos muestre la clase del error asociado a una variable por eso asociamos al error el valor de una variable
# En este caso la varible asociada es e
try:
    a=input("Ingrese un numero ")
    a/5
except Exception as e:
    print("Ha ocurrido un error=>", type(e).__name__)


        
    