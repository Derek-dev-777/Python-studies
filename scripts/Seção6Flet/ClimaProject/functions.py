import requests

#API Geocode:
# https://openweathermap.org/api/geocoding-api


api_key = "6d71fdfd13ff10ec7aa99a11cc74b58c"
cidade = "São Paulo"
pais = "BR"
url = "http://api.openweathermap.org/geo/1.0/direct?q=Niteroi,RJ,BR&appid=6d71fdfd13ff10ec7aa99a11cc74b58c"

requisicao = requests.get(url).json() 

print(requisicao)