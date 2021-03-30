# Ahora trabajaremos con las listas y las tuplas, la cuales som basicamente un conjunto ordenado de valores, ya sean variables, metodos, etc
# pero ambas tienen un gran diferencia(aparte de que se declaran de un modo diferente)

# La diferencia entre mas es que una lista es DINAMICA(puede cambiar valores)
# mientras que una tupla es ESTATICA(No puede cambiar sus valores)

# Las tuplas y listas pór igual empiezan por 0
# ¿como declaro una lista o una tupla?

#    0    1       2                 ---> ese es el orden, comienza desde 0, no desde 1
lista = [1, "Hola", True] #Declaracion de lista, siempre tienen que estar en corchetes []

tupla = (2, "adios", False) #Declaracion de una tupla

#asi es como se imprimen todos los valores de la lista o tupla

print(lista)

print(tupla)

# para cambiar el valor de la lista es con

lista[1] = "Este mensaje cambio"

# e imprimimos solo ese valor de la lista

print(lista[1])

# Los que hayan visto java lo familiarizaran con los array y la verdad si, son bastantes iguales
# TE invito a seguir progrmamndo para que pruebes :D
# Referencias
# https://recursospython.com/guias-y-manuales/listas-y-tuplas/
