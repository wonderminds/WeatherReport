import requests

def retrieve_data_from_api():
      response=  requests.get("https://api.openweathermap.org/data/2.5/weather?q=Delhi&appid=80aefbe860795a003405c3c75a97fbdb&mode=json")
      assert(response.status_code == 200), 'Status code is  not 200'
      temperature = response.json()['main']
      weather_from_api = {'feels_like':temperature['feels_like'],'High':temperature['temp_max'],'Low':temperature['temp_min'],'Humidity':temperature['humidity'],'Pressure':temperature['pressure']}
      print(weather_from_api)
