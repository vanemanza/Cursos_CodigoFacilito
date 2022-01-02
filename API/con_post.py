import requests
import json

if __name__ == '__main__':
    url = 'https://httpbin.org/post'
    payload= {
        'nombre':'vane',
        'curso':'apis con python',
        'ejemplo':'ejemplo'
    }
    """
    con metodo post vamos a crear un recurso dentro del servidor
    para eso vamos a necesitar enviar parametros, 
    vamos a enviarlos dentro del atr data. 
    El metodo post toma el diccionario y lo serializa, siempre q se lo pasemos a json,
    si colocamos los valores en el atr data, se van a enviar en form,
    para evitarlo debemos serializar data
    """
    #response = requests.post(url, json=payload) 
    response = requests.post(url, data=json.dumps(payload)) 
    print(response.url)
           
    if response.status_code == 200:     
        print(response.content)
      
      
    