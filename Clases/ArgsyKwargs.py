"""
Bien, en este punto explicare que son los kwargs y los args. Lo que tienes que entender, que estas
palabras claves sirven para manejar un numero de variable de argumentos en las funciones o los metodos

*args: Los argumentos posicionales nos permite pasar un numero de argumentos posicionales a una funcion,
       estos argumentos los reciben como una tupla.
       SINTAXIS DE ENTRADA ---> variable, variable2, variable3

       
**kwargs: Argumentos de palabras clave, este nos permite pasar un numero variable de argumentos de palabras
          clave, estos se reciben como un diccionario dentro de una funcion o metodo.
          SINTAXIS DE ENTRADA ---> variable=15, variable2="Nombre"
"""

def funcion_ejemplo(*args, **kwargs):
    """ Lineas 21-23: USO DE ARGS, LO QUE HACE ES IMPRIMIR TODAS LAS VARIABLES RECIBIDAS.
        Lineas 25-27: USO DE KWARGS, LO QUE ES IMPRIMIR LA CLAVE Y EL VALOR ENTREGADOS.
                        
    """
    
    print("Argumentos posicionales(args)")
    for arg in args:
        print(arg)
        
    print("\nArgumentos de palabras clave(kwargs)")
    for key, value in kwargs.items():
        print(key, "--->", value)

funcion_ejemplo("Hola", 1, True, nombre="Juan", edad=20)

"""
Al fin y al cabo lo que hay que entender a modo de resumen, es que los ARGS reciben los argumentos
como si fuese una tupla, mientras que los KWARGS recibe los argumentos con una llave y un valor.

Te invito a que sigas probando cosas con el arg y el kwargs, ver su utilidad, etc.
REFERENCIAS
https://j2logo.com/args-y-kwargs-en-python/
"""