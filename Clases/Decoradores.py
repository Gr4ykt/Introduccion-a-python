"""
Para empezar con decoradores tienes que entender FUNCIONES, si ta entiendes que son, el concepto, no se
te hara problema el decorador, bien. Un DECORADOR es una funcion que toma otra funcion como entrada,
esto para agregar alguna funcionalidad adicional a esa funcion y asi devolver la funcion modificada.
Esto gracias a que envolviendo la funcion original dentro de una funcion interna dentro del decorador.

Su sintaxis es sencilla que con un "@MiDecorador" lo declaras, colocando claro, sobre la funcion que se
desea decorar. Cuando se llama a la funcion decorada, lo que realmente estas llamando a la funcion interna
que crea el decorador, lo que agrega la funcionalidad adicional.

En resumen, es una funcion que modifica el comportamiento de otra funcion, lo cual aporta a que el codigo sea
mas corto.
"""

#Aqui ira un ejemplo de como funciona

#DECLARAMOS LA FUNCION DECORADOR, que recibira como argumento func
def decorador(func):
    """
        EN ESTE CASO HARE UNA FUNCION DENTRO DE OTRA PARA PODER RECIBIR BIEN LA FUNCION Y RETORNAR
        LA SALIDA SIN PROBLEMAS.
    """
    def interno():
        print("aqui inicia el decorador")
        func()
        print("Aqui finaliza el decorador")
    return interno

#AQUI COLOCAMOS LA FUNCION QUE RECIBIRA EL DECORADOR
@decorador
def funcion_decorada():
    print("Soy la funcion decorada")

#LLAMAMOS LA FUNCION DECORADA CON EL DECORADOR
funcion_decorada()

"""
REFERENCIAS
https://ellibrodepython.com/decoradores-python
"""