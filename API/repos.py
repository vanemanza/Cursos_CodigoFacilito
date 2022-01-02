import requests

client_id = '305cecbd119a50f48199'
client_secret = 'bc3434d97eaf1b79f037f6e1a26d739d0c925b87'

code = '59b0d44d871c23f88969'
access_token = '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'

if __name__ == '__main__':
    url = 'https://api.github.com/user/repos'

    headers = {'Authorization': 'token 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'}

    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        payload = response.json()

        for project in payload:
            name = project['name']
            print(name)
    else:
        print(response.content)
    
    