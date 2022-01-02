import requests

if __name__ == '__main__':
    client_id = '305cecbd119a50f48199'
    client_secret = 'bc3434d97eaf1b79f037f6e1a26d739d0c925b87'

    code = '59b0d44d871c23f88969'
    access_token = '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'

    url = 'https://api.github.com/user/repos'
    payload = {'name': 'git_api_vane'}
    headers = {'Accept': 'application/json', 'Authorization': 'token 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' }

    response = requests.post(url, headers=headers, json=payload)

    if response.status_code == 200:
        print(response.json())
    else:
        print(response.content)
