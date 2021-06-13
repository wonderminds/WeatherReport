import time
from PageObjects import Weatherpage
from PageObjects import weatherAPI
from selenium import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome('./chromedriver.exe')
weather_data={'Feels_like':''}
# function for launching the browser and navigating to specified url
def launch_browser():
    driver.get("https://weather.com/en-IN")
    driver.maximize_window()

def functionA():
      print('here we r')
# function for verifying the title of the launched page.
def verify_page_title():
       title_of_page = driver.title
       print(title_of_page)
       assert 'Local Weather', title_of_page

# function for entering the city for which temperature needs to be found
def enter_city_to_searchfor():
       try:
          search_city= Weatherpage.Search_city
          city = WebDriverWait(driver, 10).until(expected_conditions.element_to_be_clickable((By.XPATH,search_city)))
          city.send_keys("Mumbai")
          time.sleep(10)
          act = ActionChains(driver).click(city)
          act.send_keys(Keys.ARROW_DOWN, Keys.ENTER).perform()
       finally:
          print('Action performed successfully.')

def capture_weather_elements():
      try:
        Feels_like = driver.find_element_by_xpath("//span[@class='TodayDetailsCard--feelsLikeTempValue--2icPt']").text
        weather_data = {'Feels_like': Feels_like}
        High = driver.find_element_by_xpath("//*[@id='todayDetails']/section/div[2]/div[1]/div[2]/span[1]").text
        weather_data["High"] = High
        Low = driver.find_element_by_xpath("//*[@id='todayDetails']/section/div[2]/div[1]/div[2]/span[1]").text
        weather_data["Low"] = Low
        Humidity= driver.find_element_by_xpath("//*[@id='todayDetails']/section/div[2]/div[3]/div[2]/span").text
        weather_data["Humidity"]= Humidity
        pressure = driver.find_element_by_xpath("//span[@class='Pressure--pressureWrapper--3SCLm undefined']").text
        weather_data["Pressure"] = pressure
        Visibility = driver.find_element_by_xpath("//*[@id='todayDetails']/section/div[2]/div[7]/div[2]/span").text
        weather_data["Visibility"] = Visibility
        Wind = driver.find_element_by_xpath("//*[@id='todayDetails']/section/div[2]/div[2]/div[2]/span").text
        weather_data["Wind"] = Wind
        Dew_point= driver.find_element_by_xpath("//*[@id='todayDetails']/section/div[2]/div[4]/div[2]/span").text
        weather_data["Dew_point"]= Dew_point
        UV_Index= driver.find_element_by_xpath("//*[@id='todayDetails']/section/div[2]/div[6]/div[2]/span").text
        weather_data["UV_Index"]= UV_Index
        Moon_Phase= driver.find_element_by_xpath("//*[@id='todayDetails']/section/div[2]/div[8]/div[2]").text
        weather_data["Moon_Phase"]= Moon_Phase
        print(weather_data)
      finally:
        print('Operation has been completed.')

def generate_weather_report_from_API():
       weatherAPI.retrieve_data_from_api()

def comparator():
      result=  weather_data['Feels_like'] - weather_from_api['feels_like']
      if result> 3:
           print('Values lie within the acceptable ranges')
      else:
           print('Severe deviations are observed')
