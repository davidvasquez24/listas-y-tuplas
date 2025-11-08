#Operadores Aritméticos  NUMERO ASGNADO:16=REALIZAR EJERCICIOS PARES:
#1. Suma de dos números: Pide dos números y muestra su suma.

#2. Promedio: Solicita tres números e imprime el promedio.
numero_1= float(input("ingrese el primer numero: "))
numero_2= float(input("ingrese el segundo numero: "))
numero_3= float(input("ingrese el tercer numero: "))

promedio = (numero_1+numero_2+numero_3) / 3
print("el promedio es: ", promedio)

#3. Área del triángulo: Calcula el área de un triángulo con base y altura ingresadas por el usuario.

#4. Módulo: Pide dos números y muestra el residuo de su división.
num_1= float(input("ingrese primer numero: "))
num_2= float(input("ingrese segundo numero: "))

residuo= (num_1/num_2)
print("el residuo de la division es: ", residuo)

#5. Potencia: Calcula xyx^yxy usando el operador **.

#Operadores Relacionales
#6. Comparación: Solicita dos números y determina si son iguales, mayores o menores entre sí.
n_1= float(input("ingrese el primer numero: "))
n_2= float(input("ingrese el segundo numero: "))

if n_1==n_2:
    print("los dos numeros son iguales")

elif n_1>n_2:
    print("el primer numero es mayor que el segundo numero")

else:
    print("el segundo numero es mayor que el primer numero.")


#7. Verificar edad: Pide la edad y muestra si la persona es mayor de edad (≥18).

#8. Nota aprobatoria: Ingresa una calificación y verifica si es mayor o igual a 3.0.

nota=float(input("ingrese la nota"))
nota_minima_para_pasar=3.0

if  (nota>=nota_minima_para_pasar):
    print("aprobado")

elif (nota<nota_minima_para_pasar):
    print("reprobado")



#9. Comparar cadenas: Pide dos cadenas y verifica si son iguales.

#10. Número par o impar: Usa operadores relacionales y módulo para determinar si un número es par o impar.
numero=int(input("ingrese un numero: "))
if numero%2==0:
    print("el numero es par")
else: 
    print("el numero es impar: ")

#Operadores Lógicos

#11. Acceso permitido: Solicita usuario y contraseña y valida si ambos son correctos usando and.

#12. Rango de edad: Verifica si una persona tiene entre 18 y 30 años (inclusive).
edad=int(input("ingrese su edad"))
if edad>=18 and edad<=30:
    print("la persona esta dentro del rango de edad")
else:
    print("la persona NO se encuentra dentro del rango de edad")
#13. Verificación múltiple: Pide tres valores booleanos e imprime si al menos uno es True (usa or).

#14. Negación: Pregunta si llueve y usa not para imprimir si NO está lloviendo.

# Preguntar al usuario si está lloviendo
llueve = input("¿Está lloviendo? (sí/no): ").lower()
# Convertir la respuesta a un valor booleano
esta_lloviendo = llueve == "sí"
# Usar 'not' para mostrar si NO está lloviendo
if not esta_lloviendo:
    print("No está lloviendo.")
else:
    print("Sí está lloviendo.")

#15. Combinación: Determina si un número está entre 10 y 50 y es par al mismo tiempo.

#Operadores de Asignación
#16. Incremento: Declara una variable contador=0, incrementa en 1 cinco veces usando += e imprime el resultado.

# Declarar la variable contador
contador = 0
# Incrementar en 1 cinco veces usando +=
contador += 1
contador += 1
contador += 1
contador += 1
contador += 1
# Imprimir el resultado
print("El valor final del contador es:", contador)

#17. Descuento: Crea una variable precio, aplica un 20% de descuento usando *= y muestra el nuevo valor.

#18. División acumulada: Empieza con un número 100 y divídelo entre 2 tres veces usando /=.

# Declarar la variable inicial
numero = 100
# Dividir entre 2 tres veces usando /=
numero /= 2
numero /= 2
numero /= 2
print("El resultado final es:", numero)

#Operadores Bit a Bit
#19. AND bit a bit: Pide dos números enteros y muestra el resultado de &amp;.

#20. Desplazamiento: Dado un número, muestra el resultado al desplazar sus bits a la izquierda (&lt;&lt;) y a la derecha (&gt;&gt;) una posición.

# Pedir un número al usuario
numero = int(input("Ingresa un número entero: "))
# Desplazar los bits a la izquierda una posición
izquierda = numero << 1
# Desplazar los bits a la derecha una posición
derecha = numero >> 1
# Mostrar los resultados
print("Número original:", numero)
print("Desplazado a la izquierda (<< 1):", izquierda)
print("Desplazado a la derecha (>> 1):", derecha)
