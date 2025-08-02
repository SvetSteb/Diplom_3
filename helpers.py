import requests
import allure
import random
import string
import faker as f

from data import Urls
from selenium.webdriver.common.by import By

def format_locator_for_counter(locator):
    xpath = locator[1]
    formatted_xpath = f'{xpath}/div/p'
    return (By.XPATH, formatted_xpath)

def format_locator_for_order_number(number):
    format_number = f'.//p[text()="#0{number}"]'
    locator = (By.XPATH, format_number)
    return locator

def format_locator_for_order_long_number(number):
    format_number = f'.//p[text()="{number}"]'
    locator = (By.XPATH, format_number)
    return locator

def generate_random_string(length):
        letters = string.ascii_lowercase
        random_string = ''.join(random.choice(letters) for i in range(length))
        return random_string

@allure.step('Генерация новых рег.данных')
def generate_user_data():
        fake = f.Faker()
        data = {"email": f'{generate_random_string(8)}@{generate_random_string(4)}.{generate_random_string(3)}',
                "password": generate_random_string(8),
                "name": fake.first_name()}
        return data

class User:
    @staticmethod
    @allure.step('Регистрация пользователя через API')
    def register_user():
        payload = generate_user_data()
        response = requests.post(Urls.API_REG_USER, data=payload)
        auth_data = []
        if response.status_code == 200:
            auth_data = payload
        return auth_data, response   
    
    @staticmethod
    @allure.step('Удаление УЗ пользователя через API')
    def delete_user(auth_token):
        delete = requests.delete(Urls.API_DELETE_USER, headers={'Authorization': auth_token})
        return delete


