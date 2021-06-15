import requests
from PageObjects import weatherAPI

def retrieve_data_from_api():
      response=  requests.get(weatherAPI.api_url)
      assert(response.status_code == 200) is True, 'Status code is  not 200'
      temperature_from_API = response.json()['main']['temp']
      humidity_from_API= response.json()['main']['humidity']
      # weather_from_api = {'feels_like':temperature['feels_like'],'High':temperature['temp_max'],'Low':temperature['temp_min'],'Humidity':temperature['humidity'],'Pressure':temperature['pressure']}
      return(temperature_from_API,humidity_from_API)
