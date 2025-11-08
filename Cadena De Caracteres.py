#la cadena de caracteres se refiere a una serie de datos que ocupan un espacio de memoria
#ejemplo a , 1, ?;JM = y si se unen forman cadena de caracteres
#:::::::::::::::::::::::::::::::::::::::::::::::::
print("hola mundo")
print ("DAVID VASQUEZ")
curso = "programacion 1"
universidad = "sena"
print("su curso es:",curso)

institucion = "SENA" # variable tipo texto
print("su curso es:", curso, ",su  institucion es:", institucion)
trimestre = 1 #variable numerica 
print("su curso es:",curso, "su institucion es:", institucion, "su trimestre es:",trimestre)
print(len(institucion)) # el comando len sirve para contar los numeros de caracteres 
#/////////////////////////////
print(curso.upper()) #el comando upper sirve poner la cadena en MAYUSCULA 
print(curso.lower()) #el comando lower sirve poner la cadena en minuscula 
#////////////////////////////
print(institucion[0])#las corchetes sirven para traer la posicion de la cadena
print(institucion[1])#las corchetes sirven para traer la posicion de la cadena
print(institucion[2])#las corchetes sirven para traer la posicion de la cadena
print(institucion[3])#las corchetes sirven para traer la posicion de la cadena
#////////////////////////////
print(institucion[0:4]) #los corchetes y los dos puntos trae un rango de cadena
#///////////////////////////
#concatenar
print((institucion + " " + curso).upper())
#COMPARAR UNA CADENA
print(curso==institucion)#FALSO 
print (curso==universidad)#FALSO

print("analisis y desarrollo de sistemas".replace("sistemas","software")) #.rep



#
