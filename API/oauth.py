import requests

client_id = '305cecbd119a50f48199'
client_secret = 'bc3434d97eaf1b79f037f6e1a26d739d0c925b87'

code = '59b0d44d871c23f88969'
access_token = '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'
#con este valor obtengo info del usuario autenticado, username, avatar, biografia, algunos repositorios, etc
# el access token  tiene un periodo de vida aprox de 2 hs
# pero la api de github no tiene tiempo limite

#https://github.com/login/oauth/authorize?client_id=305cecbd119a50f48199&scope=respo

if __name__ == '__main__':
    
    url = 'https://github.com/login/oauth/access_token'
    payload = {'client_id': client_id, 'client_secret': client_secret, 'code': code}
    headers = {'Accept':'application/json'}

    response = requests.post(url, json=payload, headers=headers)

    if response.status_code == 200:
        response_json = response.json()

        access_token = response_json['access_token']
        print(access_token)