# son INMUTABLES

# desempaquetado / descomprimir

numeros = (1,2,3,4, 5, 6, 7, 8)
#uno, dos, tres, cuatro, *resto_valores = numeros
uno, dos, tres, cuatro, *_ = numeros #cuando quiero omitir algun valor uso _
uno, dos, tres, cuatro, *_, nueve, diez = numeros
uno, _, tres, cuatro, *_, nueve, diez = numeros

print(uno)

print(tres)
print(cuatro)
print(nueve)
print(diez)
#print(resto_valores)

# comprimir

lista = [1,2,3,4,5]
tupla = (10,20,30,40,50)

resultado = zip(lista, tupla)
resultado = tuple(resultado)
print(resultado)