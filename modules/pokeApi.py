import requests


def get_pokemon_data(pokemon_name):
    url = "https://pokeapi.co/api/v2/pokemon/" + pokemon_name
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return None
