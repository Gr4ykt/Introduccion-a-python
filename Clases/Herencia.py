"""
Que es la herencia? en la programacion orientada a objetos, la herencia consiste en la creacion de una nueva
clase en base a otra ya existente, esta clase principal conocida como CLASE PADRE, la nueva clase considerada
SUBCLASE o CLASE HIJA, hereda los atributos y metodos de la clase padre, esto no es util para reutilizar
codigo y generar una JERARQUIA DE CLASES.

Sintaxis:
    class Padre

    class hija(Padre)

Se escribe la clase de la que hereda entre parentesis.
"""

#Haremos un ejemplo con animal, el cual sera la clase padre de los animales que integremos

#creamos una clase Animal
class Animal:
    def __init__(self, nombre, tipo):
        self.nombre = nombre
        self.tipo = tipo #SERA TIPO CASERO, GRANJA, SALVAJE

    def sonido(self):
        pass        
    def retornar_tipo(self):
        return self.tipo
    
class Perro(Animal):
    def sonido(self):
        return "Guau"
    
class Gato(Animal):
    def sonido(self):
        return "Miau"
    
class Gallina(Animal):
    def sonido(self):
        return "Kikiriki"
    
perro1 = Perro("Toby", "Casero")
gallina1 = Gallina("Juancha", "Granja")
gato1 = Gato("Manchas", "Casero")

print(perro1.sonido())
print(gato1.retornar_tipo(), gato1.sonido())
print(gallina1.sonido())

"""
REFERENCIAS
https://ellibrodepython.com/herencia-en-python
"""