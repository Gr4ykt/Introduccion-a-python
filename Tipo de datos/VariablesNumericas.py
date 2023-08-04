# Pese a que el mismo titulo de esto habla de por si solo, las variables son un gran modo de almacenar datos muy utilizados en la programación
# empezar con este es sencillo, basta con saber darle un valor a algo, entender los numeros en la programacion y como funcion, que para eso
# esta esta pequeña guia para que puedas saber cosa basicas sobre programación

# antes de empezar a declarar alguna variable, hay que entender los tipos de variables numericas que existen dentro del mundo de la programación
# pero bueno, empezare explicando los tipos que hay, son 3 de los cuales te hablare aqui, ya que en python se utilizan 3 de modo mas basico
# bueno sin mas rollo, empiezo.

# enteras    --->  int  ---> 1,2,3,4,5,6,7,123541...
# flotantes  ---> float ---> 2.3;2.1312314....
# long       ---> long  ---> 44L o mas infinito, mayormente utilizado para evitar desbordamientos de buffer
# Complex    ---> Te invito a que lo busques ;)

# hay una serie de reglas a seguir a la hora de declarar variables, ya que hay palabras reservadas por el lenguaje
# o simplemente, su sentencia es erronea
# aqui puedes encontrar estas reglas https://www.openbookproject.net/thinkcs/archive/python/thinkcspyesp3e_abandonado/cap02.html

#empezemos a programar!! :)
# en python a diferencia de otros lenguajes no es necesario escribir al inicio el tipo de variable a declarar
# el presente ejempo es para diferenciar el entero entre una variable en JAVA y PYTHON

#JAVA   ---> int a = 5;
#PYTHON ---> a = 5

var_entero   = 5 # variable entera(INT)
var_flotante = 5.57 # variable flotante(FLOAT)

# La coma es para separar datos, ya que si se introduce directamente en la cadena de texto, nos devuleve las "var_entero", no el resultado que almacena
print("variable entera: ", var_entero)

print("variable flotante: ", var_flotante)

# para saber el tipo de variable que se esta almacenando en python basta con "type(variable)"
# ejemplo con el entero

print(type(var_entero))

# HORA DE RETO!!!
# Te invito a que desarrolles un programa en el que declares una variable e imprimas el tipo de variable, animo!! ;)

# referencias
# https://www.tutorialpython.com/variables-en-python/
# https://entrenamiento-python-basico.readthedocs.io/es/latest/leccion3/tipo_numericos.html
