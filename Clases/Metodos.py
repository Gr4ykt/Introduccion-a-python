"""
Una vez visto los concceptos de constructor, clases y objetos, es hora de conocer los metodos.
Que es un metodo?
Un metodo con lo visto hasta ahora es una funcion dentro de una clase, la gran diferencia es que 
la funcion es un bloque de codigo independiente, mientras que el metodo es similar a la funcion,
pero este tiene una diferencia y es que el metodo ESTA ASOCIADO A UN OBJETO, este puede acceder
a los atributos que posea la clase a traves de la palabra clave self. Si bien recuerdas, el SELF 
hace referencia a la clase en la cual estas trabajando.
Pues no hay mas que decir sobre los metodos, es una funcion que trabaja bajo un objeto, estos se
declaran en la clase y trabajan bajo ese contexto.
"""

#DECLARAMOS LA CLASE CON SU CONSTRUCTOR
class Auto:
    def __init__(self, color, marca, patente):
        self.color = color
        self.marca = marca
        self.patente = patente
    
    #Aqui colocamos los metodos, si recuerdas, el constructor(__init__) es un metodo especial de python
    
    #CREAREMOS UN METODO QUE IMPRIMA LA INFO DEL AUTO
    def imprimirInfo(self):
        #SOLO POR ESTA VEZ UTILIZARE EL PRINT EN UN METODO, YA QUE ES MALA PRACTICA UTILIZARLOS ASI
        print("Informacion del auto\n", "Color: ", self.color, "\n", "Marca: ", self.marca, "\n", "Patente: ", self.patente, "\n")
    
#Creamos un objeto para utilizar el metodo
miAuto = Auto("Azul", "Toyota", "7F34HG")
autoVecino = Auto("Blanco", "Mazda", "JSL34TR")

#Llamamos al metodo
miAuto.imprimirInfo()
autoVecino.imprimirInfo()

"""
Bien, ahora que esta explicado lo basico para las clases es hora de comenzar con lo fuerte, ya que las clases
poseen herencia, polimorfismo y encapsulamiento y argumentos posicionales en conjunto a las argumentos de palabras clave

REFERENCIAS
https://programacion.net/articulo/como_funcionan_las_clases_y_objetos_en_python_1505
"""