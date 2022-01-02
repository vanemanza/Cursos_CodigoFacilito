import requests

"""
realizo una peticion a los servidores de google
e imprimo lo que me regresa.
"""
if __name__ == '__main__':
    url = 'https://www.google.com.mx/'
    response = requests.get(url)

    #print(response)
    """
    al ejecutar el archivo la respuesta sera:
    <Response [200]> que es el status de la peticion que nos 
    devuelve el servidor
    """    

    if response.status_code == 200:
        #print(response.content)
        """
        al volver a ejecutar el servidor obtenemos todas las etiquetas
        html q conforman la pagina web
        """
        content = response.content
        file = open('google.html', 'wb')
        file.write(content)
        file.close()
        """
        con el contenido q nos regresa el servidor, podemos almacenar
        el contenido de la pagina, para eso creamos una variable content
        generno un archivo, en este caso google.html
        y al ejecutar se genera un nuevo archivo q guarda todas las 
        etiquetas
        """

