import time
from enum import Enum
from Base.WebDriver import GetWebDriver
from PageObjects import Weatherpage
from selenium import webdriver
from selenium.webdriver.remote.webelement import  WebElement
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.action_chains import  ActionChains

class Utils:
         def __init__(self,driver):
              Browser = input('Enter the browser you want to launch')
              driver = GetWebDriver.get_webdriver(Browser)
              self.driver= driver


         def open(self):
            url= Weatherpage.application_url
            self.driver.get(url)
            time.sleep(5)
            self.driver.maximize_window()

         def retrieve_using(self,strategy_locator):
            if '_' not in strategy_locator:
                  strategy_locator = Strategy.ID.value + '_' + strategy_locator
            strategy_and_locator= str(strategy_locator).split('_')
            strategy = strategy_and_locator[0]
            locator =  strategy_and_locator[1]
            using = None
            if strategy == Strategy.XPATH.value:
                 using = (By.XPATH,locator)
            elif  strategy== Strategy.ID.value:
                 using = (By.ID,locator)
            elif strategy == Strategy.CSS.value:
                using = (By.CSS_SELECTOR,locator)
            elif strategy == Strategy.TAGNAME.value:
                 using = (By.TAG_NAME,locator)
            elif strategy == Strategy.NAME.value:
                  using = (By.NAME,locator)
            return using

         def find_element(self,locator):
            return self.driver.find_element(self.retrieve_using(strategy_locator=locator))

         def click_on_element(self,locator):
            element = None
            if isinstance(locator,str):
                element = self.find_element(locator)
            elif isinstance(locator,WebElement):
                element = locator
            if element is not None:
                element.click()

         def get_textvalue(self,locator):
              if isinstance(locator,WebElement):
                  element = locator
              else:
                  element= self.find_element(locator)
              return element.text

         def send_keys(self,locator,*keys):
            element = self.wait_until_element_present(locator)
            try:
                 element.sendkeys(*keys)
            except Exception as exc:
                raise exc


         def wait_until_element_present(self,locator,timeout=10):
                try:
                    element= WebDriverWait.until(expected_conditions.visibility_of_element_located(self.retrieve_using(locator)))
                    return element
                except Exception as element_not_present_exc:
                    raise element_not_present_exc

         def wait_until_element_clickable(self,locator,timeout=15):
                 try:
                      element = WebDriverWait.until(expected_conditions.element_to_be_clickable(self.retrieve_using(locator)))
                      return element
                 except Exception as element_not_clickable_exc:
                      raise element_not_clickable_exc

         def move_and_click_element(self,locator):
            if isinstance(locator,WebElement):
                element= locator
            else:
                element= self.find_element(locator)
            try:
                 act = ActionChains()
                 act.move_to_element(locator).click().perform()
            except Exception as exc1:
                raise exc1

class Strategy(Enum):
     XPATH= "xpath"
     ID= "id"
     CSS= "css"
     TAGNAME= "tag name"
     NAME= "name"

