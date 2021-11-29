lista = ['String', 10, 15.6, True] #list()

print(lista)


lista_cursos = ['Python', 'Django', 'Flask', 'Ruby', 'Java']

primer_curso = lista_cursos[0]
print(primer_curso)

segundo_curso = lista_cursos[1]
print(segundo_curso)

ultimo_curso = lista_cursos[4] #lista_cursos[-1]
print(ultimo_curso)

lista_cursos[4]  = 'Rust'
print(lista_cursos)

sub_lista = lista_cursos[0:3] 
print(sub_lista)

#[start:end] el último elemento no es incluido en la lista
#[start:] obtengo desde start hasta el último elemento 
#[:end] obtengo desde el primer hasta end
#[start:end:skip] el tercer parametro es un salto,en este caso de dos en dos
# [:] genero una sublista con todos los elem de la lista original
#[::2]toda la lista de dos en dos
#[::-1]genero una sublista del ultimo al primero

sub_lista = lista_cursos[0:5:2]
print(sub_lista)

sub_lista = lista_cursos[::2]
print(sub_lista)

sub_lista = lista_cursos[::-1]
print(sub_lista)

lista_cursos.append('MongoDB') #agrega un elem al final
print(len(lista_cursos))

lista_cursos.insert(1, 'Rails') #primer parametro el indice donde lo quiero agregar
print(lista_cursos)

lista_cursos_2 = ['C', 'C++', 'Docker']
lista_cursos.extend(lista_cursos_2)
print(lista_cursos)

lista_cursos.remove('MongoDB')
print(lista_cursos)

del lista_cursos[0] #se usa el indice q quiero eliminar
print(lista_cursos)

lista_cursos.clear() #elimina todos los elementos
print(len(lista_cursos))


