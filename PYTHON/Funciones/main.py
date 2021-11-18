"""
def suma():
    numero_uno = int(input('ingrese un numero:  '))
    numero_dos = int(input('ingrese otro numero:  '))
    resultado = numero_uno + numero_dos
    print(resultado)

suma()    
"""
"""
def suma(n1, n2):
    resultado = n1 + n2
    print(resultado)

numero_uno = int(input('ingrese un numero:  '))
numero_dos = int(input('ingrese otro numero:  '))
    
suma(numero_uno, numero_dos)   
"""

def suma(n1, n2):
    #resultado = n1 + n2
    #return resultado
    return n1 + n2, 'Retorno un str' #puedo retornar n cantidad de valores, recomendado max 3

numero_uno = int(input('ingrese un numero:  '))
numero_dos = int(input('ingrese otro numero:  '))
    
#resultado = suma(numero_uno, numero_dos)  
resultado, mensaje = suma(numero_uno, numero_dos)#uso desempaquetado de tuplas para retornar dos valores 
#resultado, _ = suma(numero_uno, numero_dos) puedo omitir el segundo valor
print(resultado) 
print(mensaje)
