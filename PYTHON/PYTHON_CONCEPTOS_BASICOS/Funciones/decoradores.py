# sirven para reducir lineas de código
# Un decorador es una funcion q toma como input otra funcion y retorna otra funcion

"""
a = Funcion principal ( decorador)
b = Funcion a decorar 
c = funcion decorada

a(b) -> c
"""
# Lo usamos para extender funcionalidades a una funcion que
"""
def funcion_a(funcion_b):

    def funcion_c():
        print('>>> Antes del llamado')
        funcion_b()
        print('>>> Despues del llamado')
    return funcion_c 

@funcion_a # con esta linea le indico a Python q la funcion_a 
            # va a recibir como argumento a la funcion saludar q es la
            #que quiero decorar

def saludar():
    print('Hola funcion Saludar')

@funcion_a
def suma():
    print(10+30)


saludar()   
suma()
"""

# si la funcion a decorar recibe parametros y retorna valores

def funcion_a(funcion_b):
    
    def funcion_c(*args, **kwargs):
        print('>>> Antes del llamado')
        resultado = funcion_b(*args, **kwargs)
        print('>>> Despues del llamado')
        return resultado
    return funcion_c 

@funcion_a
def suma(n1, n2):
    return n1 + n2

resultado = suma(10, 20)    
print(resultado)