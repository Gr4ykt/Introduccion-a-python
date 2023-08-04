"""
Si entendiste que son las clases y los objetos, junto a los metodos esta parte sera pan comido, dire 
desde ahora que ire con el concepto de autos como clases en toda esta seccion, pero te invito que veas 
otras cosas de la vida real y las vuelvas codigo, como un arbol, los animales, personas, cliente, etc, 
incluso simular algun tipo de cuenta bancaria, etc.

Bien, que es un constructor?
Para que nuestra clase tenga ATRIBUTOS requiere de un CONSTRUCTOR, un constructor es un metodo especial,
recuerdas los metodos en la parte de METODOS? Pues tienes que saber que existen metodos especiales
que utiliza el lenguaje, uno de ellos es el metodo __init__, este metodo se ejecuta automaticamente al
crear un objeto y su funcion es que este inicializar los atributos creados en la clase, esto se hace bajo
una sintaxis la cual va bajo el un codigo "self" para definir que se crearan esos atributos en los objetos

El SELF es mas para referenciar al objeto que esta siendo creado bajo la clase, lo cual permitira acceder
y modificar los atributos de la clase.
"""

#Siguiendo lo de la clase auto, haremos su constructor
class Auto:
    #METODO ESPECIAL INIT CON SU SELF REFERENCIANDO A LA CLASE
    def __init__(self, color, marca):
        """
            Para crear un atributo debemos colocarlo en los objetos de la funcion
            y luego referenciar a la clase con self.
        """
        self.color = color
        self.marca = marca

# Creamos el objeto, pero esta vez dentro de los parentesis colocamos los atributos de este
miAuto = Auto("Rojo", "Mazda")

#IMPRIMIMOS EL COLOR DEL AUTO DEL OBJETO miAuto 
print(miAuto.color)

"""
Te invito a que practiques este concepto, para ir conociendolo mejor y dominarlo, tranquilo, no todo
saldra a la primera, tu sigue intentando.
Como reto te invito a que CREES UNA CLASE PERSONA, QUE POSEA EL ATRIBUTO EDAD, NOMBRE, APELLIDO.

REFERENCIAS
https://programacion.net/articulo/como_funcionan_las_clases_y_objetos_en_python_1505
"""