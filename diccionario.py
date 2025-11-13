# ----------------------------------------------
# DICCIONARIOS Y SETS EN PYTHON - EXPLICACIÓN
# ----------------------------------------------

# DICCIONARIO:
# Un diccionario en Python es una colección no ordenada de elementos que se almacenan como pares clave:valor.
# Cada clave dentro del diccionario debe ser única, y se accede al valor a través de su clave.
# Los diccionarios se definen usando llaves {}, por ejemplo:
# persona = {"nombre": "Ana", "edad": 25}
# Son mutables (se pueden modificar), y muy útiles para representar objetos, registros, etc.
# Ejemplo de uso de un diccionario:
persona={
    "nombre": "juan",
    "edad": 24,
    "profesion": "estudiante"
}
print("diccionario completo",persona)
print("nombre:", persona["nombre"]) 
print("edad:", persona["edad"])
print("profesion:", persona["profesion"])
persona["edad"]=25
print("edad actualizada:", persona["edad"])
