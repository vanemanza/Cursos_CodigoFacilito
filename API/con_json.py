import requests
import json

if __name__ == '__main__':
    url = 'https://httpbin.org/get'
    args= {
        'nombre':'vane',
        'curso':'apis con python',
        'ejemplo':'ejemplo'
    }

    response = requests.get(url, params=args)
    print(response.url)
           
    if response.status_code == 200:     
        """
        forma usando diccionarios de python
        """   
        """
        response_json = response.json() #dict
        origin = response_json['origin']
        print(origin)
        """

        """
        forma utilizando la libreria json, debo importarla
        """
        response_json = json.loads(response.text)
        origin = response_json['origin']
        print(origin)

    
       

