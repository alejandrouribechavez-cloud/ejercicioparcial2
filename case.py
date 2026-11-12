name=[]
lastname=[]
age=[]
email=[]
password=[]
confirmpass=[]
opcion=[]

print("Bienvenido al sistema de registro de cliente")
print("menu principal")
print("1. Registrar cliente")
print("2. ver informacion del cliente")
print("3. borrar informacion del cliente")
print("4. modificar informacion del cliente")
print("5. salir")
print("--------------------------------")
opcion=int(input("Ingrese una opcion: "))

match opcion#Aqui inicia el match, que es una validacion de caso

case 1: 

name=input("Ingrese su nombre: ")
lastname=input("Ingrese su apellido: ")
age=int(input("Ingrese su edad: "))
birtday=input("Ingrese su fecha de nacimiento: ")
email=input("Ingrese su correo electronico: ")
password=input("Ingrese su contraseña: ")
confirmpass=input("Confirme su contraseña: ")
case 2:

print("nombre:",name,"edad:",age,"fecha de nacimiento:",birtday,"correo electronico:",email,"contraseña:",password)
case 3:

name=""
lastname=""
age=0
birtday=""
email=""
password=""
case 4:

name=input("Ingrese su nombre:")
lastname=input("Ingrese su apellido:")
age=int(input("Ingrese su edad:"))
birtday=input("Ingrese su fecha de nacimiento:")
email=input("Ingrese su correo electronico:")
password=input("Ingrese su contrasena:")
case 5:

print("Hasta luego!")
case_:
print("Opcion no valida,")