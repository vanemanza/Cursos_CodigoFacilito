# Docstrings
# El docstring queda almacenado en el atributo __doc__
#  Objetos documentables ( __doc__): Módulos, Clases, Métodos y Funciones

def suma(n1, n2):
    """
    La funcion suma 2 numeros enteros. #breve descripcion de la tarea q realiza la funcion
    Argumentos: # detallar las partes de la funcion
    n1 (int)
    n2 (int)

    Se retorna la suma de los parametros.
    
    >>> suma(10, 20)
    30

    >>> suma(100, 200)
    30
        
    """
    return n1 + n2 

# print(suma.__doc__)    # imprimo lo q el atributo doc almacena
# o con la funcion help
print(help(suma))

#-------------------------------------------------

# Podemos testear las funciones usando el docstring -->

# python -m doctest documentar.py