#Las funciones recursivas, te recomiendo repasar antes la clase de FUNCIONES para entender mejor esta parte
#bien, empecemos, las funciones recursivas son funciones que se llaman a si mismas, la verdad es que de
"""
Una funcion recursiva es un tipo de funcion que se llama asi misma en su entorno,
utilidad no poseen mucho, es mejor utilizar bucles, pero bueno, nunca esta demas aprender a 
utilizarlos, no?
"""

#El ejemplo es el ingreso de una password con una serie de intentos

#creamos una funcion
def login(intentos = 3):
    if intentos > 0:#si intentos en mayor que 0
        print("\nIntentos disponibles: {0}".format(intentos))
        entrada_pass = input("Ingrese password: ") #aqui ingresamos cantidad de intentos
        print("Comprobando....")
        if entrada_pass == "pepito123": #password pepito123
            print("Password correcta, Bienvenido <3")
            exit(0) #Codigo de salida exitoso
        else: #Caso de contrasena incorrecta
            print("Password incorrecta")
            return login(intentos - 1)#en caso de ser incorrecta vuelve a retornar login pero en este caso en vez de ser 3, seran 2 debido a intentos -1
    else:
        print("No te quedan mas intentos :(")

login()

#Te invito a que veas otros casos de funciones recursivas para entenderlos mejor