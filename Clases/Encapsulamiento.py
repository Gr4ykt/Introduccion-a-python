"""
Esta parte sera bastante corta, ya que nada mas sera para explicar el CONCEPTO DE ACCESO, veras,
en la POO existen modo de dejar los datos y los metodos, esto bajo algo conocido como ENCAPSULAMIENTO.
Este concepto consiste en ocultar los detalles internos de una clase y permitir un acceso controlado
a los atributos y metodos desde el exterior. Es una forma de proteger y organizar la implementacion de
la clase, asegurando que los cambios internos no afecten al codigo, esto se logra a traves de 3 tipos
de datos o metodos:

    1. PUBLICO: Accesibles desde cualquier parte del codigo dentro o fuera de la clase, no posee
                restricciones de acceso y su definicion es solo colocando el nombre de atributo o
                metodo a generar.
    2. PROTEGIDOS: Los metodos o atributos protegidos indica que no puede ser accedido desde fuera
                   de la clase, pero aun se puede acceder a ellos desde fuera si se desea, pero,
                   se considera mejor optar por no acceder a ellos directamente desde fuera de la
                   clase. Su definicion es bastante sencilla ya que basta con tan solo aplicar 
                   un guion bajo"_" al principio del nombre (_nombre).
    3. PRIVADOS: Metodos o atributos poco accesibles, ya que python utiliza "Name Mangling", esto hace
                 que el nombre real sea modificado, se puede acceder a este desde fuera con el nombre
                 modificado, pero es mala practica. Para definir es a diferencia del PROTEGIDOS, este
                 es con doble guion bajo"__" al principio del nombre (__nombre).
"""

#Para este ejemplo simulare el funcionamiento de un banco, para entender mejor el concepto
class Persona:
    """
    A TENER EN CUENTA
        El str(algo) es para tranformar a string ya que como int no retorna con la concatenacion de cadenas
    """
    
    #constructor
    def __init__(self, nombre, edad):
        self.nombre = nombre #Publico
        self._edad = edad    #Protegido
        self.__saldo = 1000  #Privado 
    
    #acceder a atributo privado
    def retornar_info(self):
        return "Nombre: " +  self.nombre + " -- " + "Edad: " + str(self._edad) + " -- " + "Saldo: [ACCESO CON CLAVE]"
    
    #metodo protegido
    def _incrementar_edad(self):
        self._edad += 1
        
    #metodo privado
    def __aumentar_saldo(self, cantidad):
        self.__saldo += cantidad
    #metodo privado
    def __restar_saldo(self, cantidad):
        self.__saldo -= cantidad
    
    #ACCEDER A LOS METODOS PRIVADOS
    def recibir(self, cantidad):
        return self.__aumentar_saldo(cantidad)
    
    def transferir(self, cantidad):
        return self.__restar_saldo(cantidad)
    
    def obtener_saldo(self, clave):
        if clave == "secreto":
            return "$" + str(self.__saldo)
        else:
            return "Clave incorrecta"
        
Juan = Persona("Juan Rodriguez", 30)
print(Juan.retornar_info())

print(Juan.obtener_saldo("secreto")) #Retornar saldo del objeto "Juan Rodriguez"
Juan.transferir(300)
Juan.recibir(2500)
print(Juan.obtener_saldo("secreto"))

Juan._incrementar_edad()
print(Juan.retornar_info())

"""
Espero que el concepto haya quedado claro, te invito a que programes utilizando encapsulamiento para
entenderlo mejor, happy hacking!! :)

REFERENCIAS
https://ellibrodepython.com/encapsulamiento-poo
"""