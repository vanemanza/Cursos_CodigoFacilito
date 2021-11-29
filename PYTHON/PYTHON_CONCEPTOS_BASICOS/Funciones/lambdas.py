"""
def centigrados_a_farenheit(grados):
    return grados * 1.8 + 32

mi_funcion = centigrados_a_farenheit #si le pongo () la estoy llamando desde la variable, pero solo quiero asignarla
print(mi_funcion(10)) 
# le paso los argumentos cuando la llamo, pero ahora con el nombre de la variable
"""

funcion_grados = lambda grados: grados * 1.8 + 32

#estructura con parametros obligatorios
#lambda <parametro> : <expresion de la funcion>

print(funcion_grados(10))

# ej sin parametros
sin_parametros = lambda : True 

#con dos parametros x default
parametros_default = lambda p1=10, p2=20 : p1 + p2

#con asterisco
asterisco = lambda *args, **kwargs: len(args) + len(kwargs)


