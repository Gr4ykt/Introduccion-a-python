"""
Para empezar esta parte del curso, tenemos que explicar que es una clase y que es un objeto, bien.

Que es una clase?
En el paradigma de la programacion orientada a objetos o mas conocida como POO es indispensable las
clases y los objetos, esto debido a que la POO esta orientada a la creacion de objetos, en un ejemplo
sencillo es como verlo como algo del entorno real, un objeto puede ser un auto, pero el objeto auto
nace de la clase Auto para existir, esta sencillo no?
Esto tiene una utilidad dentro de la programacion, ya que los objetos pueden ser tipos de datos,
tales como los que se usaron, como los int, list, dict, estos tipos de datos SON OBJETOS que provienen
de la clase con sus respectivos nombres, en la programacion esta es la utilidad que se le da a los
objetos y las clases, crear tipos de datos, entre otras utilidades.

Que es un objeto?
El objeto es a lo que se le denomina instancia de una clase, esta funciona entregando los atributos
que la clase posee, y poder llamar los metodos creados en esta, tanquilo, ya explicare mas adelante que son
estos.

A lo que quiero llegar es que la POO funciona bajo ese concepto, crear tipos de datos, mayormente este
se enseña con objetos de la vida real, lo cual no es mal concepto, pero la idea va un poco mas alla,
tienes que entender que bajo la linea de la programacion esto tiene su funcion para crear tipos de datos,
estos datos que provienen de la clase.
"""

# Vamos a ver un ejemplo sencillito, ya que hablamos de autos, pero iremos paso a paso
# Creamos una clase llamada Auto bajo la siguiente sintaxis, recordar, 
# ES BUENA PRACTICA QUE LOS NOMBRES DE LAS CLASES INICIEN CON UNA MAYUSCULA 
class Auto:
    pass #ESTO ES PARA QUE LA CLASE NO HAGA NADA, YA VEREMOS QUE HACE ESTO

#Ahora se crea el objeto
miAuto = Auto() # ESTE ES EL OBJETO

autoDeVecino = Auto() # este es OTRO OBJETO

"""
Espero se entienda el concepto, si entendiste bien te recomiendo seguir en el METODOS, ve poco a poco
Happy Hacking!! :)

REFERENCIAS
https://programacion.net/articulo/como_funcionan_las_clases_y_objetos_en_python_1505
"""