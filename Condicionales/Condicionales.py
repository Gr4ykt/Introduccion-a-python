"""
Aqui se empieza a tensar que te cagas, es broma, los condicionales no son dificiles de entender, en pocas palabras como su propio
nombre lo dice tienen como objetivo una condicion, si esto es igual que aquello, me haces esto, en caso de que sea esto en vez de
esto me haces esto otro, y si no es ninguno de los dos hazme esto ¿comprendes?

los principales comandos para estas condiciones lo son:
IF : Si la condicion es verdadera
ELIF : En caso alterno pero no falsa
ELSE: En caso sea falsa

tambien hay que tener en cuenta los operadores logicos a la hora de programar asi, te los dejare por aqui para que los veas

esta and, or y not, sus mismas palabras te diran que son

tambien hay que tener en cuenta los operadores de variables

	a > b --> a es mayor que b
	a < b --> a es menor que b
	a == b --> a es igual que b
	a != b --> a es diferente a b
	a >= b --> a es mayor o igual que b
	a <= b --> a es menor o igual que b
"""

# Pequeño programa de condicionales
a = 5 #Puedes cambiarme para ver los diferentes resultados
b = 3 #Puedes cambiarme para ver los diferentes resultados

if a > b and b < a: # siempre al comenzar una secuencia abajo, tienes que tabular
	print("a es mayor que b")
elif a < b or b > a:
	print("b es mayor que a")
else:
	print(False)

# no justamente tienen que dar estos resultados, puedes ir probando programando condicionales para comprenderlos mejor

#RETOOOOOO!!! :D
# TE invito a que programes un condicional que me diga si es mayor de edad o no, y en caso de poner un numero mayor a 100 arrojar un false, Vamos!! :D

# Referencias
# https://www.mclibre.org/consultar/python/lecciones/python-if-else.html
# https://entrenamiento-python-basico.readthedocs.io/es/latest/leccion4/operadores_logicos.html
