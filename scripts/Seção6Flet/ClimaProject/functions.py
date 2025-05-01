import requests

# API Geocode (usada para buscar as cordenadas das cidades que serão digitadas):
# https://openweathermap.org/api/geocoding-api

# API ipInfo (usada para pegar as cordenadas atuais do usuario):
# https://ipinfo.io/

#API
# https://openweathermap.org/current#name




api_key = "6d71fdfd13ff10ec7aa99a11cc74b58c"

# Função para pegar as cordenadas da cidade informada.
"""
Exemplo de como usar a função de buscar as cordenadas da localização digitada pelo usuario

lati,long = cords_by_name(apiKey="6d71fdfd13ff10ec7aa99a11cc74b58c",city="Balneario Camboriu", country="BR")

print(lati,long)

"""
def cords_by_name(apiKey, city, country, country_code=None, limit=1):
    
    if country_code:
        location = f"{city},{country_code},{country}"
    else:
        location = f"{city},{country}"
    
    url = f"http://api.openweathermap.org/geo/1.0/direct?q={location}&limit={limit}&appid={apiKey}"

    cords_request = requests.get(url).json() 

    return cords_request[0]["lat"], cords_request[0]["lon"]

# Função para pegar as cordenadas do usuario ( baseadas no ip do mesmo )

"""
Exemplo de como usar a função de buscar as cordenadas atuais do usuario

user_lat, user_long = get_user_cords()
print(user_lat,user_long)

"""
def get_user_cords():

    url = "https://ipinfo.io/"

    ip_request = requests.get(url).json()

    user_cords = ip_request["loc"].split(",")

    user_lat = user_cords[0]
    user_long = user_cords[1]

    return user_lat,user_long

# Função para buscar as informações do tempo na cordenada desejada pelo usuario

def previsao_tempo(user_lat, user_long, api_key):

    url = f"https://api.openweathermap.org/data/2.5/weather?lat={user_lat}&lon={user_long}&appid={api_key}"

    requisicao = requests.get(url).json()

    return requisicao

cordenadas_dadas_user = cords_by_name(api_key,"São Paulo","Brazil")
previsao = previsao_tempo(cordenadas_dadas_user[0],cordenadas_dadas_user[1],api_key)

print(cordenadas_dadas_user[0])
print(cordenadas_dadas_user[1])
print(previsao)