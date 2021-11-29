#parametros obligatorios
"""
def area_circulo(radio, pi):
    return pi * (radio**2)

resultado = area_circulo(10, 3.14) 
print(resultado)   
"""

#parametros x default
"""
def area_circulo(radio, pi=3.14):
    return pi * (radio**2)

resultado = area_circulo(10) 
print(resultado)   
"""
# nombrar los argumentos cuando llamo la funcion permite llamarlos en cualquier orden
def area_circulo(radio, pi=3.14):
    return pi * (radio**2)

resultado = area_circulo(pi=3.141592, radio=10) #igual al metodo format
print(resultado)   

