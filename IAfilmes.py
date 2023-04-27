import requests
import json
import random 

# Insira sua chave de API aqui
API_KEY = "d4f37601d786141550b835c23ab6e2c6"

# URL da API para filmes populares
URL = f"https://api.themoviedb.org/3/movie/popular?api_key={API_KEY}"

# Faz uma solicitação GET para a API e armazena a resposta em um objeto JSON
response = requests.get(URL)
movies = json.loads(response.text)["results"]

# Seleciona um filme aleatório e exibe o título e a sinopse
selected_movie = movies[random.randint(0, len(movies)-1)]
print("Filme sugerido:")
print(selected_movie["title"])
print(selected_movie["overview"])
