from py.xml import html
import pytest
from  Base.WebDriver import GetWebDriver


@pytest.fixture(scope='class')
def setup(request, browser):
    teardown_flag = False
    driver = GetWebDriver.get_web_driver(browser)
    driver.maximize_window()
    request.cls.driver = driver
    failed_before = request.session.testsfailed
    yield
    if request.session.testsfailed != failed_before:
        teardown_flag = True
        request.cls.weather.teardown_browser()
    if not teardown_flag:
        request.cls.weather.teardown_browser()


@pytest.fixture(scope='class')
def browser(request):
    "pytest fixture for browser"
    return request.config.getoption("-B")


def pytest_addoption(parser):
    parser.addoption("-B", "--browser",
                     dest="browser",
                     default="chrome",
                     help="Browser. Valid options are firefox and chrome")


@pytest.mark.optionalhook
def pytest_html_report_title(report):
    report.title = "Test Results"


@pytest.mark.optionalhook
def pytest_configure(config):
    platform = config._metadata.get('Platform', '')
    config._metadata = dict()
    config._metadata['Platform'] = platform
    config._metadata['Browser'] = config.getoption("-B")


@pytest.mark.optionalhook
def pytest_html_results_table_header(cells):
    cells.insert(0, html.th('TC No.', class_="sortable numeric", col="tc_no"))
    cells.insert(1, html.th('Description'))
    cells.pop(3)
    cells.pop()
    
number = incrementor()


@pytest.mark.hookwrapper
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    if report.when == "call":
        sr_no = number()
        report.tc_no = str(sr_no)
        city = item.instance.report_city
        report.description = str(item.function.__doc__) + city




