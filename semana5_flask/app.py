from flask import Flask, render_template
import urllib.request, json

app = Flask(__name__)

@app.route("/")
def get_list_characters_page():
    url = "https://rickandmortyapi.com/api/character/"
    response = urllib.request.urlopen(url)
    data = response.read()
    dict = json.loads(data)
    
    return render_template("characters.html", characters=dict["results"])


@app.route("/profile/<id>")
def get_profile(id):
    url = "https://rickandmortyapi.com/api/character/" + id
    response = urllib.request.urlopen(url)
    data = response.read()
    dict = json.loads(data)
    
    return render_template("profile.html", profile=dict)





@app.route("/lista")

def get_list_characters():
    
    url = "https://rickandmortyapi.com/api/character/"
    response = urllib.request.urlopen(url)
    characters = response.read()
    dict = json.loads(characters)
    
    characters = []
    
    for character in dict["results"]:
        character = {
            "name": character["name"],
            "status": character["status"]
        }
        characters.append(character)
    return {"characters": characters}


# 1. Criar uma nova rota para listar as localizações. A rota deverá ser
# acessível através do caminho /locations. A página deverá ser
# renderizada através do template locations.html. A página deverá
# conter uma tabela com as seguintes informações: nome, tipo e
# dimensão. A tabela deverá conter um link para a página de perfil
# da localização.

@app.route("/locations")
def get_locations():
    
    url = "https://rickandmortyapi.com/api/location/"
    response = urllib.request.urlopen(url)
    data = response.read()
    locations = json.loads(data)
    
    return render_template("locations.html", locations=locations["results"])

# 2. Criar uma nova rota para listar os episódios. A rota deverá ser
# acessível através do caminho /episodes. A página deverá ser
# renderizada através do template episodes.html. A página deverá
# conter uma tabela com as seguintes informações: nome, data de
# lançamento e código. A tabela deverá conter um link para a
# página de perfil do episódio.
@app.route("/episodes")
def get_episodes():
    
    url = "https://rickandmortyapi.com/api/episode/"
    response = urllib.request.urlopen(url)
    data = response.read()
    episodes = json.loads(data)
    
    return render_template("episodes.html", episodes=episodes["results"])

@app.route("/episodes/<id>")
def get_episode(id):
    url = "https://rickandmortyapi.com/api/episode/" + id
    response = urllib.request.urlopen(url)
    data = response.read()
    episodes = json.loads(data)
    
    characters_by_episode = []
    for character_url in episodes["characters"]:
        character_id = character_url.split("/")[-1]
        character = get_profile_by_episode(character_id)
        characters_by_episode.append(character)
        
    return render_template("episode.html", episode=episodes, characters=characters_by_episode)

def get_profile_by_episode(id):
    url = "https://rickandmortyapi.com/api/character/" + id
    response = urllib.request.urlopen(url)
    data = response.read()
    characters = json.loads(data)
    
    return characters

