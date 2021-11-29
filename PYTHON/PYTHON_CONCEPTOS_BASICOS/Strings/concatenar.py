nombre = 'Vanesa María'
apellido = 'Manzanelli'

#nombre_completo = nombre + ' ' + apellido

#nombre_completo = 'Mr. %s %s %s.'%(nombre, apellido, 'Perez')

#metodo format
#nombre_completo = 'Mr. {} {}.'.format(nombre, apellido, 'Perez')
"""
nombre_completo = 'Mr. {nombre} {apellido}.'.format(
    nombre=nombre,
    apellido=apellido,
)"""
#print(nombre_completo)

nombre_completo = f'Mr. {nombre} {apellido}.'

print(nombre_completo)