f = open("archivo.txt", "r")


#readline usado de esta forma nos devuelve la primer y segunda linea, si agrego un tercero uso devuelve la tercera
# print(f.readline())
# print(f.readline())

# readlines devuelve lista de string de cada linea que tenemos
print(f.readlines())
      
# f.write("Esto es un texto")
# f.write("Esto es un texto pero segundo")
# f.write("Esto es un texto pero tercero")

# content = f.read()
# print(content)
#con w modifica la info ya existente, si cambiamos la w por a es cuando crea nueva info sin pisar la existente
# r nos permite


#Metodo seek devuelve un indice al cual volver
print(f.read())
print("Esto es despues del primer read ********************")

#Metodo seek hace que se empiece desde el caracter indicado como argumento en este caso el 20
f.seek(20)
print("Esto es despues del segundo read ***************")
print(f.read())
f.close()

