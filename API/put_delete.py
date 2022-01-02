import requests
import json

if __name__ == '__main__':
    url = 'https://httpbin.org/put'
    payload= {
        'nombre':'vane',
        'curso':'apis con python',
        'ejemplo':'ejemplo'
    }
    headers = {'Content-Type': 'application/json', 'access-token': '123456'}
    response = requests.put(url, data=json.dumps(payload), headers=headers) 
    print(response.url)
           
    if response.status_code == 200:     
        #print(response.content)
        headers_response = response.headers
        #print(headers_response)
        server = headers_response['server']
        print(server)

"""
para delete reemplazo put x delete
"""        