import pytest
from helpers import *
from selenium import webdriver

from pages.main_page import MainPage
from pages.auth_page import AuthorizePage
from pages.queue_page import QueuePage


@pytest.fixture
def new_user():
    result = User.register_user()
    auth_token = result[1].json().get('accessToken')
    yield result
    User.delete_user(auth_token)

@pytest.fixture(params=["chrome", "firefox"])
def driver(request):
    if request.param == 'chrome':
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--window-size=1920,1080')
        driver = webdriver.Chrome(options=chrome_options)
    else:
        driver = webdriver.Firefox()

    yield driver
    driver.quit()

@pytest.fixture
def main_page(driver):
    page = MainPage(driver)
    page.driver.get(Urls.MAIN_PAGE)
    return page

@pytest.fixture
def queue_page(driver):
    queue_page = QueuePage(driver)
    queue_page.driver.get(Urls.QUEUE_PAGE)
    return queue_page

@pytest.fixture
def auth_page(driver):
    auth_page = AuthorizePage(driver)
    auth_page.driver.get(Urls.AUTH_PAGE)
    return auth_page
