import pytest
# from Base import WebDriver
import self as self

from Base.Utilities import Utils
from Base import Weather_Report
from Base import Weather_API

by = None
we = Utils(driver='edge')
we.open()
by = we.find_element(self,'xpath')
#we.find_element(self,by)
print(by)


    # def po(self,request):
    #     weather = Weather_Report(self.driver)
    #     weather_api = Weather_API()
    #     request.cls.weather = weather
    #     request.cls.weather_api = weather_api
    #
    # def temp_variance(self,city):
    #     variance = 3
    #     temperature_from_UI = self.weather.retrieve_temp(city)
    #     temperature_from_API= self.weather_api.retrieve_data_from_api()
    #     difference = temperature_from_UI - temperature_from_API
    #     assert (difference<=variance) is True, 'Temperature variation is out of acceptable limit'
    # def humidity_variance(self,city):
    #     variance= 3
    #     humidity_from_UI= self.weather.retrieve_humidity()
    #     humidity_from_API= self.weather_api.retrieve_humidity()
    #     difference = humidity_from_UI - humidity_from_API
    #     assert(difference<=variance) is True, 'Humidity is out of acceptable limit'

