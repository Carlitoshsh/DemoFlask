from flask import Flask
from modules.pokeApi import get_pokemon_data 

app = Flask(__name__)


@app.route("/<pokemon_name>")
def not_care(pokemon_name):
    return get_pokemon_data(pokemon_name)
