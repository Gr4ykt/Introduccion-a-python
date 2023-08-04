"""
En python, existen palabras claves para los bucles, estos cumplen funciones especificas, y poseen
sus utilidades, estos con el break, continue, pass(ESTE NO SOLO TIENE UTILIDAD DENTRO DE LOS BUCLES)

Definiciones:

    CONTINUE: Este sirve para saltar a la siguiente iteracion sin ejecutar el resto del codigo
    
    BREAK: Para terminar abruptamente el bucle y salirse de las iteraciones, en pocas palabras,
           rompe el bucle, y no continua con las iteraciones
    
    PASS: Es una palabra clave que no hace nada, su utilidad es para marcar posicion cuando una sintaxis
          requiere instruccion pero no hemos definido alguna accion a ejecutar.
"""

opciones = """
Opciones:
\t(1) Continuar el programa
\t(2) Salir del programa
\t(3) Pasar a la siguiente iteracion
"""
inicio = 1

while True:
    print("Numero de iteraciones:", inicio)
    print(opciones)
    opcion = int(input(">> "))
    
    if opcion == 1:
        print("Seleccionaste continue, pasaste a la siguiente iteracion")
        inicio += 1
        continue
    elif opcion == 2:
        print("Utilizaste break, rompiste el bucle")
        break
    elif opcion == 3:
        print("Utilizaste pass")
        pass
    else:
        print("selecciona una de las 3 opciones")
        inicio -= 1
    
    inicio += 1