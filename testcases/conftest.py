import pytest
from selenium import webdriver

@pytest.fixture
def oneTimeSetup(request,scope='class'):
    baseUrl = "https://www.carwale.com/"
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(baseUrl)
    driver.implicitly_wait(4)
    if request.cls is not None:
        request.cls.driver = driver
    yield driver
    driver.quit()

