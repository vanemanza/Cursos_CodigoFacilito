titulo = 'Curso de Python'

#for caracter in titulo:
    #print(caracter)
"""
for caracter in titulo:
    if caracter == ' ':
        break #permite finalizar de forma inmediata cualquier ciclo
    print(caracter)    
"""
for caracter in titulo:
    if caracter == ' ':
        continue #hace q el ciclo salte a la siguiente iteracion y no se ejacuta lo q se encuentre despues
    print(caracter)    