####=============FORMULARIO============0
print("FORMULARIO DE USUARIOS")
nombre = input ("ingrese su nombre numero uno")
nombre2 = input("ingrese su segundo nombre")
apellido = input ("ingrese su apellido")
apellido2 = input("ingrese su segundo apellido")
print("el nombre completo es: ", nombre + " " + nombre2 +  " " + apellido +  " " + apellido2)

#=================DATOS NUMERICOS========
# --- FORMULARIO DE DATOS PERSONALES ---

# Entrada de datos
edad = int(input("Ingrese su edad: "))
peso = float(input("Ingrese su peso (kg): ").replace(",", "."))
telefono = int(input("Ingrese su teléfono: "))
altura = float(input("Ingrese su altura (m): ").replace(",", "."))
hijos = int(input("Ingrese número de hijos: "))
año_nacimiento = int(input("Ingrese su año de nacimiento: "))
mes_nacimiento = int(input("Ingrese su mes de nacimiento: "))
dia_nacimiento = int(input("Ingrese su día de nacimiento: "))
cedula = int(input("Ingrese su número de cédula: "))

# Limpieza de pantalla (solo decorativo, no borra realmente)
print("\n" + "="*40)
print("📋  FICHA DE DATOS NUMÉRICOS  📋")
print("="*40)

# Salida de datos formateada
print(f"{'Edad:':25} {edad} años")
print(f"{'Peso:':25} {peso} kg")
print(f"{'Teléfono:':25} {telefono}")
print(f"{'Altura:':25} {altura} m")
print(f"{'Número de hijos:':25} {hijos}")
print(f"{'Año de nacimiento:':25} {año_nacimiento}")
print(f"{'Mes de nacimiento:':25} {mes_nacimiento}")
print(f"{'Día de nacimiento:':25} {dia_nacimiento}")
print(f"{'Cédula:':25} {cedula}")
print("="*40)
print("✅ Registro completado con éxito.")


#===================DATOS TEXTO O STRING==============
# --- FORMULARIO DE DATOS DE TEXTO ---

# Entrada de datos
correo = input("Ingrese su correo electrónico: ")
tipo_de_sangre = input("Ingrese su tipo de sangre: ")
genero = input("Ingrese su género: ")
estado_civil = input("Ingrese su estado civil: ")
eps = input("Ingrese su EPS: ")
universidad = input("Ingrese su universidad: ")
carrera = input("Ingrese su carrera: ")

# Decoración del encabezado
print("\n" + "="*45)
print("💬  FICHA DE DATOS DE TEXTO  💬")
print("="*45)

# Salida formateada
print(f"{'Correo electrónico:':25} {correo}")
print(f"{'Tipo de sangre:':25} {tipo_de_sangre}")
print(f"{'Género:':25} {genero}")
print(f"{'Estado civil:':25} {estado_civil}")
print(f"{'EPS:':25} {eps}")
print(f"{'Universidad:':25} {universidad}")
print(f"{'Carrera:':25} {carrera}")

print("="*45)
print("✅ Registro completado con éxito.")

#EJERCICIO MOSTRAR EL FORMULARIO LLENO