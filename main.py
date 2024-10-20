# Comment se connecter a une API avec Python
import requests

# URL de base de l'API à utiliser
base_url = "https://pokeapi.co/api/v2/"

# Fonction pour obternir des informations sur un pokémon spécifique par son nom
def get_pokemon_info(name):
    # URL pour le pokémon spécifique
    url = f"{base_url}/pokemon/{name}"
    # Envoyer un requête 'GET' à l'API et si c'est réussi (code 200), alors analyser la réponse en JSON
    reponse = requests.get(url)
    print(reponse)
    if reponse.status_code == 200:
        pokemon_data = reponse.json()
        return pokemon_data
    else:
        # Si la requête a échoué, afficher le message d'erreur
        print(f"Échec de la récupération des données {reponse.status_code}")

# Définir le nom du pokémon à récupérer (e.p: patrat, pikachu,Watchog, Rattata...)
pokemon_name = "patrat"
# Appeler la fonction pour obtenir les informations du pokémon
pokemon_info = get_pokemon_info(pokemon_name)

# Si les informations du Pokémon sont récupérées avec un succès, afficher les détails pertinents
if pokemon_info:
    print(f"Nom: {pokemon_info["name"].capitalize()}")
    print(f"Id: {pokemon_info["id"]}")
    print(f"Taille: {pokemon_info["height"]}")
    print(f"Poids: {pokemon_info["weight"]}")