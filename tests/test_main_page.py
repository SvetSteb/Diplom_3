import allure
import pytest
import time

from locators.main_page_locators import MainPageLocators
from data import Urls
from pages.main_page import MainPage
from pages.auth_page import AuthorizePage

@allure.feature("Тестирование функционала главной страницы")
class TestMainPage:

    @pytest.mark.parametrize('locator, check_locator, result_text', [
                            (MainPageLocators.CONSTRUCTOR, MainPageLocators.CONSTRUCTOR_TITLE, "Соберите бургер"),
                            (MainPageLocators.QUEUE, MainPageLocators.QUEUE_TITLE, "Лента заказов")
    ])
    @allure.title('Тестирование перехода с главной страницы по кнопкам Кноструктор, Лента действий')
    @allure.description('''1. Перейти на главную страницу
                           2. Клик по кнопке (locator)
                           ОР: Заголовок страницы(check_locator) соответствует заданному (result_text)''')
    def test_button_on_main_page(self, main_page, locator, check_locator, result_text):
        main_page.wait_for_and_click_element(locator)
        result = main_page.wait_for_visibiliti_of_element(check_locator)
        assert result.text == result_text


    @pytest.mark.parametrize('ingredient_locator, count_expect',[(MainPageLocators.BUN_1, '2'),
                                                          (MainPageLocators.SAUSE_1, '1')])
    @allure.title('Тест изменения счетчика количества при добавлении ингридиентов в корзину')
    @allure.description('''1. Перейти на главную страницу
                           2. Перетащить ингридиент в конструктор(корзину) (ingredient_locator)
                           ОР: Счетчик ингридиентов изменился  (count_expect)''')
    def test_put_ingredient_in_bascet(self, main_page, ingredient_locator, count_expect):
        count_fact = main_page.put_one_ingredient(ingredient_locator)
        assert count_fact == count_expect


    @allure.title('Тест наличия модального окна с информацией об ингридиенте')
    @allure.description('''1. Перейти на главную страницу
                           2. Кликнуть на ингридиент
                           ОР: На странице появилось окно с заголовком "Детали ингредиента"''')
    def test_ingredient_info_modal_window(self, main_page):
        ingredient_window = main_page.click_on_ingredient()
        assert ingredient_window.text == "Детали ингредиента"


    @allure.title('Тест закрытия модального окна')
    @allure.description('''1. Перейти на главную страницу
                           2. Кликнуть на ингридиент
                           3. Кликнуть на иконку закрытия - крестик
                           ОР: Окно более не отображается на странице''')
    def test_close_ingredient_info(self, main_page):
        modal_window = main_page.click_on_ingredient()
        main_page.close_modal_window()
        assert modal_window.is_displayed() is False
        
        
    @allure.title('Тест авторизованный пользователь может оформить заказ')
    @allure.description('''Прудсловие: создать новго тестового пользователя
                           1. Перейти на главную страницу
                           2. Выбрать булочку
                           3. Выбрать наполнитель
                           3. Кликнуть заказать
                           ОР: Номер в появившемся окне не равен 9999
                           Постусловие: удалить тестового пользователя''')
    def test_order_burger_by_authorize_user(self, driver, new_user):
        driver.get(Urls.MAIN_PAGE)
        main_page = MainPage(driver)
        main_page.click_on_personal_account()
        auth_page = AuthorizePage(driver)
        auth_page.authorization(new_user[0])
        order_number = main_page.order_burger()
        assert order_number != '9999'

