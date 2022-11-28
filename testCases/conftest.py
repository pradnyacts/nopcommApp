from selenium import webdriver
import pytest

@pytest.fixture()
def setup(browser):
    if browser=='chrome':
        driver= webdriver.Chrome()
        print("chrome browser")
    elif browser=='firefox':
        driver = webdriver.Firefox()
        print("firefox browser")
    else:
        driver = webdriver.Chrome()

    return driver

def pytest_addoption(parser):
    parser.addoption("--browser")

@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")

#### pytest html report#####
# It is hook for adding env info to html report
def pytest_configure(config):
    config._metadata['Project name']= 'nop commerce'
    config._metadata['Module name']= 'Customers'
    config._metadata['Tester'] = 'Pradnya'

#hook to delete/modify env info to html report
@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)

