# How to connect to an API using Python
import requests

base_url = "https://pokeapi.co/api/v2/"

def get_pokemon_info(name):
    url = f"{base_url}/pokemon/{name}"
    reponse = requests.get(url)
    print(reponse)
    if reponse.status_code == 200:
        print ("Data retrieved!")
    else:
        print(f"Failed to retrieve data {reponse.status_code}")

pokemon_name = "pikachu"
get_pokemon_info(pokemon_name)