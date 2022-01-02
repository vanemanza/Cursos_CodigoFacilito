import requests

def get_pokemons(url='https://pokeapi.co/api/v2/pokemon-form', offset=0):
    
    args = {'offset': offset} if offset else {}

    response = requests.get(url, params=args)
    
    if response.status_code == 200:

        payload = response.json()
        results = payload.get('results', [])

        if results:
            for pokemon in results:
                name = pokemon['name']
                print(name)

        next = input("seguir listando? si o no:    ").lower()
        if next == 'si':
            get_pokemons(offset=offset+20)

if __name__ == '__main__':
    url = "https://pokeapi.co/api/v2/pokemon-form"
    get_pokemons()
    