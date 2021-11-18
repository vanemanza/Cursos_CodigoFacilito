# son funciones q se usan de argumentos de otras funciones
# son llamadas x las funciones q reciben los argumentos

promedio = lambda *args : sum(args) / len(args)

aprobado = lambda calificacion : calificacion >= 7

print(promedio(10,10,9,8,7))
print(aprobado(5))

def mostrar_mensaje(fun1, fun2, *args):
    promedio = fun1(*args)

    if fun2(promedio):
        print(f'Aprobaste')
    else:
        print(f'no aprob')    

mostrar_mensaje(promedio, aprobado, 10,10,8,7,7)