from PageObjects import Setup_env
from PageObjects import weatherAPI

# function for launching the browser and navigating to specified url


def launch_browser_and_verify_title():
    Setup_env.launch_browser()
    Setup_env.verify_page_title()

# function for providing the city for which temperature needs to be find and generate the temperature report
def generate_weather_report():
    Setup_env.enter_city_to_searchfor()
    Setup_env.capture_weather_elements()

def weather_report_from_API():
    Setup_env.generate_weather_report_from_API()

def comparison():
     Setup_env.comparator()


