#LISTAS EN PYTHON
#las listas son datos que tienen como caracteristicas ser mutables 
#las listas son ordenadas
#Ejemplo
estudiante=["ERIK","ZULETA","ANGIE","KAROL", "LEONARDO"]
print(estudiante) #IMPRIMIR LA LISTA 
print(len(estudiante)) 
print(estudiante[2])
estudiante[2]
print(estudiante)
estudiante.append("DIEGO")
print(estudiante)
estudiante.remove("ERIK")
print(estudiante)
del estudiante
print("mostrar todas las frutas")
for estudiante in estudiante:
    print (" ", estudiante)
     
#================================
#=============TUPLAS=============
#================================
#LAS TUPLAS SON ORDENADAS
#LAS TUPLAS NO SON MUTABLES
#LAS TUPLAS SE DEFINEN CON ()
equipos = ("nacional", "millonarios", "santafe", "junior")
print(equipos)
print("")
