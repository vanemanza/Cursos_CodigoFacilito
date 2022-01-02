import requests

if __name__=='__main__':
    url = 'https://api.github.com/user'

    session = requests.session()
    session.auth = ( 'vanemanza1@gmail.com', 'VaneDev2021')

    response = session.get(url, )
    if response.ok:
        print(response.content)
    else:
        print(response.content)    