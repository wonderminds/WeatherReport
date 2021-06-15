from selenium import webdriver
from selenium.webdriver import DesiredCapabilities
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

# this class is used for launching the desired browser
class GetWebDriver:


        def get_webdriver(browser):
                if browser.casefold() == 'edge':
                   return webdriver.Edge("C:\\Useful_SW\\edge_driverV91\\msedgedriver.exe")
                elif browser.casefold() == 'chrome':
                     options= webdriver.ChromeOptions()
                     preferences = {'safebrowsing.enabled':'false'}
                     desired_Caps= DesiredCapabilities.CHROME
                     options.add_experimental_option("prefs",preferences)
                     return webdriver.Chrome("C:\\Useful_SW\\ChromeV91\\chromedriver.exe",chrome_options=options,desired_capabilities=desired_Caps)


