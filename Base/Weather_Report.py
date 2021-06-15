from Base import Utilities

from PageObjects import Weatherpage

class Weather_Report(Utilities.Utils):
      temperature_from_UI = None
      def __init__(self,driver):
         super().__init__(driver)
         self.driver= driver

      def search_for_city(self,city):
         url = Weatherpage.application_url
         self.open(self,url)
         locator= Weatherpage.Search_city
         self.send_keys(self,locator,city)

      def retrieve_temp(self,city_name):

          try:
            temperature_from_UI= Weatherpage.current_weather_from_UI
            locator = 'xpath'
            temperature_from_UI= Utilities.wait_until_element_present(self,locator,timeout=15)
            temperature_from_UI= temperature_from_UI.text
          except Exception as element_not_present_exc:
             raise element_not_present_exc
          finally:
             return temperature_from_UI

      def retrieve_humidity(self):
             humidity= None
             try:
                humidity_from_UI = Weatherpage.current_humidity_from_UI
                locator = 'xpath'
                humidity_from_UI = Utilities.wait_until_element_present(self,locator,timeout=10)
                humidity_from_UI= humidity_from_UI.text
             except Exception as element_not_present_exc:
                  raise element_not_present_exc
             finally:
                 return humidity_from_UI

