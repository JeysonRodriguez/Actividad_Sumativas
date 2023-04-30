import requests

# Definimos las URLs base de la API
BASE_URL = "https://swapi.dev/api/"
PLANETS_URL = BASE_URL + "planets/"
PEOPLE_URL = BASE_URL + "people/"
STARSHIPS_URL = BASE_URL + "starships/"

# Definimos una función para hacer solicitudes GET a la API
def make_request(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return None

# a) ¿En cuántas películas aparecen planetas cuyo clima sea árido?
# Hacemos una solicitud GET a la API para obtener la lista de planetas
planets_response = make_request(PLANETS_URL)
if planets_response is not None:
    arid_planets = [planet for planet in planets_response["results"] if "arid" in planet["climate"]]
    # Imprimimos el número de películas en las que aparecen estos planetas
    films = set()
    for planet in arid_planets:
        for film_url in planet["films"]:
            film = make_request(film_url)
            if film is not None:
                films.add(film["title"])
    print(f"Hay {len(films)} películas en las que aparecen planetas con clima árido.")

# b) ¿Cuántos Wookies aparecen en la sexta película?
# Hacemos una solicitud GET a la API para obtener la lista de personajes
people_response = make_request(PEOPLE_URL)
if people_response is not None:
    wookies = [person for person in people_response["results"] if "wookiee" in person["species"]]
    # Buscamos el número de Wookies que aparecen en la sexta película
    wookies_in_sixth_movie = 0
    for wookie in wookies:
        for film_url in wookie["films"]:
            film = make_request(film_url)
            if film is not None and "Return of the Jedi" in film["title"]:
                wookies_in_sixth_movie += 1
    print(f"Hay {wookies_in_sixth_movie} Wookies en la sexta película.")

# c) ¿Cuál es el nombre de la aeronave más grande en toda la saga?
# Hacemos una solicitud GET a la API para obtener la lista de naves espaciales
starships_response = make_request(STARSHIPS_URL)
if starships_response is not None:
    # Encontramos la nave espacial con el tamaño máximo
    largest_starship = max(starships_response["results"], key=lambda x: int(x["length"]))
    print(f"La aeronave más grande en toda la saga se llama {largest_starship['name']} y mide {largest_starship['length']} metros de largo.")