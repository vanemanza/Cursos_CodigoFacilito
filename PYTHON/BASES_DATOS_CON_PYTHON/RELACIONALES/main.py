import MySQLdb


""" para q podamos realizar una conexion a la db,
    usamos la libreria MySQLdb con el método connect
    Que recibe 4 parametros->
    MySQLdb.connect(host, username, password, namedb)

    Para q el código quede mas legible, conviene declarar los 
    parametros antes como constantes. 

    host = donde se encuentra la base de datos
    username = con el cual nos podemos conectar a la db
    password = de dicho username
    namedb = nombre de la base de datos

    El método connect regresa un objeto connect q puedo almacenar
    en una variable conection
"""
"""
esa es la conexion y siempre hay q cerrarla cuando no la voy a usar mas.
"""   

"""
el cursor sirve para poder tener una interaccion con la db,
"""
# con estas lineas puedo hacer una conexion a mi db

HOST = 'localhost'
USER = 'root'
PASSWORD = ''
DATABASE = 'curso_python'

if __name__ == '__main__':
    connection = MySQLdb.connect(HOST, USER, PASSWORD, DATABASE) # abre la conexion

    cursor = connection.cursor()

    connection.close() # cierra la conexion
 

    