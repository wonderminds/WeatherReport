import pytest
from PageObjects import weatherAPI
from PageObjects import Weatherpage
from PageObjects import Configuration as config

@pytest.mark.usefixtures('setup', 'po')
class TestComparator:
    @pytest.fixture(scope='class')
    def po(self, request):
        weather = Weatherpage(self.driver)
        weather_api = weatherAPI()
        request.cls.weather = weather
        request.cls.weather_api = weather_api

    @pytest.mark.parametrize('city', config.cities)
    def test_temperature_variance(self, city):
        self.city= city
        temp_variance= config.variance
        temperature_from_UI= self.retrieve_temp(self,city)
        temperatur_from_API= self.weather_api.retrieve_data_from_api(city)

        temp_diff= abs(temperature_from_UI - temperature_from_API)
        assert (temp_diff<= temp_variance) is True, 'Variation is out of acceptable range'

    @pytest.mark.parametrize('city',config.cities)
    def test_humidity_variance(self,city):
        self.city= city
        humidity_variance= config.humidity_variance
        humidity_from_web = self.weather.retrieve_humidity(city)
        humidity_from_API= self.weather_api.retrieve_data_from_api(city)
        humidity_diff= abs(humidity_variance - humidity_from_API)
        assert (humidity_diff<= humidity_variance) is True, 'Humidity is out of acceptable range'
