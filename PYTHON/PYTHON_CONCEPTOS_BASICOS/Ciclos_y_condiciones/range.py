#rango = range(11) #coloco el valor final q no es tomado en cuenta


for valor in range(5,21,3): #valor inicial, final menos uno, y salto o skip

    print(valor)
#print(type(rango))

numeros = [10,20,30,40,50]

for indice, numero in enumerate(numeros, 10): #le puedo pasar como segundo argumento en q numero quiero q comience el indice
    print(indice, numero)
