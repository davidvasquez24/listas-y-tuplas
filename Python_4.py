# # Ejercicios Listas y Tuplas

# # Ejercicios con Listas
# # 1. Rotación de Playlist Musical
# #Tienes una lista con el orden de canciones de una playlist
# Escribe un programa que pida al usuario un número n y rote la lista de canciones n posiciones a la
# derecha.
# # Ejemplo
# playlist = ["Canción A", "Canción B", "Canción C", "Canción D"]
# # Sin = 2 - ["Canción C", "Canción D", "Canción A", "Canción B"]
playlist = ["cancion 1", "cancion 2", "cancion 3", "cancion 4", "cancion 5"]
n = int(input("Ingrese el número de posiciones para rotar la playlist: "))
n = n % len(playlist)  # Asegurarse de que n no sea mayor que la longitud de la lista
rotated_playlist = playlist[-n:] + playlist[:-n]
print("Playlist rotada:", rotated_playlist)


# 2. Filtrar Ingredientes Prohibidos
# Un chef tiene una lista de ingredientes para una receta.
# Escribe un programa que pida al usuario los ingredientes que no quiere (pueden ser varios, separados
# por coma) y genere una nueva lista eliminando los ingredientes prohibidos.
# python
# CopiarEditar
# # Ejemplo
# ingredientes = ["harina", "huevo", "leche", "azúcar", "chocolate"]
# # Prohibidos: huevo, leche -+ ["harina", "azúcar", "chocolate"]

ingredientes = ["pasta", "leche", "tomate", "cebolla", "carne molida de res", "ajo", "salsa boloñesa"]
prohibidos_input = ("Ingrese los ingredientes prohibidos, separados por comas: ")
print("Ingredientes prohibidos:", prohibidos_input)
print("la nueva lista de ingredientes teniendo en cuenta los requerimientos del cliente son: ", ingredientes.remove(ingredientes[prohibidos_input]))

