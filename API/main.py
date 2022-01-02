import requests

"""
realizo una peticion usando el metodo get a httpbin.org
"""
if __name__ == '__main__':
    #url = 'https://httpbin.org/get?nombre=vanesa&curso=apis&nada=todo'
    #envio de parametros usando get
    
    'para enviar parametros de forma dinamica los paso con un dic args'
    url = 'https://httpbin.org/get'
    args= {
        'nombre':'vane',
        'curso':'apis con python',
        'ejemplo':'ejemplo'
    }

    response = requests.get(url, params=args)
    # para ver como está conformada la url:
    print(response.url)
    """
    el metodo get se encarga de construir la url a partir de los
    parametros q nosotros le enviemos.
    """
        
    if response.status_code == 200:        
        content = response.content
        print(content)
    
       

