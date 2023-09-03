import requests
import config

canton_capital_dict = {
    "Aargau": "Aarau",
    "Appenzell Ausserrhoden": "Herisau",
    "Appenzell Innerrhoden": "Appenzell",
    "Basel-Landschaft": "Liestal",
    "Basel-Stadt": "Basel",
    "Bern": "Bern",
    "Fribourg": "Fribourg",
    "Geneva": "Geneva",
    "Glarus": "Glarus",
    "Graubünden": "Chur",
    "Jura": "Delémont",
    "Lucerne": "Lucerne",
    "Neuchâtel": "Neuchâtel",
    "Nidwalden": "Stans",
    "Obwalden": "Sarnen",
    "Schaffhausen": "Schaffhausen",
    "Schwyz": "Schwyz",
    "Solothurn": "Solothurn",
    "St. Gallen": "St. Gallen",
    "Thurgau": "Frauenfeld",
    "Ticino": "Bellinzona",
    "Uri": "Altdorf",
    "Valais": "Sion",
    "Vaud": "Lausanne",
    "Zug": "Zug",
    "Zurich": "Zurich"
}

for key, val in canton_capital_dict.items():
    city_name = val
    limit = 1
    loc_api_url = f'http://api.openweathermap.org/geo/1.0/direct?q={city_name}&limit={limit}&appid={config.API_key}'
    loc_api_response = requests.get(loc_api_url)
    lat = loc_api_response.json()[0]['lat']
    lon = loc_api_response.json()[0]['lon'] 
    weather_api = f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={config.API_key}&units=metric'
    weather_api_response = requests.get(weather_api)
    temp = weather_api_response.json()['main']['temp']
    weather = weather_api_response.json()['weather'][0]['main']
    distinct_weather = weather_api_response.json()['weather'][0]['description'] 
    # TO DO - Confirm that is switz town 
    canton_capital_dict[key] = {'city_name': city_name,
                                'temp': temp,
                                'weather': weather,
                                'distinct_weather': distinct_weather}
    print(canton_capital_dict[key])
    
    
    # api delivery - https://openweathermap.org
     
    # Start work on a different branch
    # READ IT https://www.dataquest.io/blog/python-api-tutorial/
   