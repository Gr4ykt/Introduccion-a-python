"""
Antes de pasar polimorfismo, te recomiendo que veas HERENCIA, ya que es util para entender el polimorfismo.
El polimorfismo consiste en la capacidad que poseen los objetos de diferentes clases de ser utilizados de
manera uniforme debido a que comparten una interfaz en comun.

Un buen ejemplo serian los animales, si bien recuerdas de herencia, todos los animales tenian una funcion,
la que se llamaba "sonido", esta es una funcion en comun, la cual puede ser utilizada con polimorfismo, 
ahora veremos como utilizarlo.

Creare la misma clase animal de la cual heredaran los demas, luego veremos el proceso del polimorfismo.
"""

class Animal:
    """NO LLEVARA CONSTRUCTOR YA QUE TAN SOLO UTILIZARE ESTA FUNCION"""
    def sonido(self):
        pass
    
class Perro(Animal):
    def sonido(self):
        return "Guau guau"
    
class Gato(Animal):
    def sonido(self):
        return "Miau"

class Vaca(Animal):
    def sonido(self):
        return "Muuuu"
    
#HAREMOS DOS FORMAS DE IMPRIMIR EL POLIMORFISMO

#============================Forma 1=======================================
def hacer_sonido(animal):
    return animal.sonido()


perro = Perro()
gato = Gato()

print(hacer_sonido(perro))
print(hacer_sonido(gato))
#===========================================================================
print("=================================================================")
#============================Forma 2=======================================

for animal in Perro(), Gato(), Vaca():
    print(animal.sonido())

#===========================================================================

"""
Espero hayas entendido el concepto de polimorfismo, sino es asi, te invito a investigar, es uno de
los procesos que requiere la programacion, la investigacion, te invito a revisar las referencias,
te dejare tambien el Duck typing o tipado dinamico para que le heches una leida. Te felicito, haz
terminado clases, te inivito a seguir programando y viendo conceptos, practicarlos y entenderlos de 
mejor modo, espero haberte sido util.

REFERENCIAS
https://ellibrodepython.com/polimorfismo-en-programacion
https://ellibrodepython.com/duck-typing-python
"""