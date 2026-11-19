name=[]
lastname=[]
age=[]
email=[]
password=[]
confirmpass=[]
opcion=0

while True:
    print("Bienvenido al sistema de registro de cliente")
    print("menu principal")
    print("1. Registrar cliente")
    print("2. ver informacion del cliente")
    print("3. borrar informacion del cliente")
    print("4. modificar informacion del cliente")
    print("5. salir")
    print("--------------------------------")
    opcion=int(input("Ingrese una opcion: "))

    match opcion:#Aqui inicia el match, que es una validacion de caso

        case 1:

            name=(input("Ingrese su nombre:"))
            lastname=(input("Ingrese su apellido:"))
            age=int(input("Ingrese su edad:"))
            birtday=(input("Ingrese su fecha de nacimiento:"))
            email=(input("Ingrese su correo electronico:"))
            password=(input("Ingrese su contraseña:"))
            confirmpass=(input("Confirme su contraseña:"))
        case 2:
                print("lista de clientes registrados:")
                for i in range(len(name)):
                    print("id:-", i,"con el nombre:", name[i],"con el apellido:", lastname[i],"con la edad de:", age[i])
         case 3:

            index=int(input("ingresa el indice de clientes a borrar(empezando desde 0):"))
        case 4:

            name=(input("Ingrese su nombre:"))
            lastname=(input("Ingrese su apellido:"))
            age=int(input("Ingrese su edad:"))
            birtday=(input("Ingrese su fecha de nacimiento:"))
            email=(input("Ingrese su correo electronico:"))
            password=(input("Ingrese su contrasena:"))
        case 5:

            print("Hasta luego!")
            case_:
            print("Opcion no valida,")