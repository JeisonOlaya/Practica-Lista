#Nombre, apellido, correo y edad
usuarios = []

Menu = True

while Menu:      
    print("=="*20,"\n")
    print("Bienvenido a la base de datos de estudiante \nActualmentete presentamos nuestro menu de opciones.\n")
    print("=="*20,"\n")
    
    print("1.) Crear Usuario")
    print("2.) Lista de Usuario")
    print("3.) Editar Usuarios")
    print("4.) Eliminar un Usuario\n")

    escoger = int (input ("Que opcion elijes: \n"))
    if escoger == 1:
        continuar = True
        while continuar: 
            nombre = input("ingresa el nombre: ")

            apellido = input("por favor ingresa el apellido: ")


            correo = input("por favor ingrese el correo: ")


            edad = input("por favor ingresa la edad: ")
            usuarios.append([nombre,apellido,correo,edad])

        
            valor = input(" desea continuar agregando nombres: S(si) N(no)?: ")
            if valor == "N" or valor =="n":
                continuar = False
        print("haz creado el usuario correctamente")
        

        volver = int(input("para volver al menu anterior, digita 1, o 2 para finalizar: "))
        if volver==2:
            print ("exitoso ")
            Menu = False

    if escoger == 2:
        print("La lista de usuario es: \n")
        contador = 0
        for recorrer in usuarios:            
            print(contador,".)", recorrer[0],recorrer[1],recorrer[2],recorrer[3])
            contador = contador + 1
        print("")

        
        
        volver = int(input("para volver al menu anterior, digita 1, o 2 para finalizar: "))
        if volver==2:
            print ("exitoso ")
            Menu = False
        

"""if volver == 1: 
    print("1.) Crear Usuario")
    print("2.) Lista de Usuario")
    print("3.) Editar Usuarios")
    print("4.) Eliminar un Usuario\n")"""


    

    
