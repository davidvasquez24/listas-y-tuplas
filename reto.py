#crear el correo institucional con la primera letra del primer nombre, la inicial del segundo nombre, primer apellido completo, inicial segundo apellido, terminado en @sena.edu.co
nombre1 = "JUAN"
nombre2 = "DAVID"
apellido1 = "VASQUEZ"
apellido2 = "RODRIGUEZ"

print("su correo institucional es:",(nombre1[0]+nombre2[0]+apellido1+apellido2[0]).lower()+"@sena.edu.co")
