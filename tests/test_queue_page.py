import allure
import pytest

from locators.queue_page_locators import QueueLocators
from pages.main_page import MainPage
from pages.queue_page import QueuePage
from pages.auth_page import AuthorizePage

@allure.feature("Тестирование функционала Лента заказов")
class TestQueuePage:

    @allure.title('Тест детали заказа в ленте заказов')
    @allure.description('''1. Перейти на ленту заказов
                           2. Выбрать заказ
                           ОР: Окно  с инфо о заказе отображено''')
    def test_order_info_window_is_displayed(self, queue_page):
        info_window = queue_page.click_on_order_info()
        assert info_window.is_displayed() is True


    @allure.title('Проверка отображения заказа из истории заказов пользователя в ленте заказов')
    @allure.description('''Предусловие: в системе создан пользователь
                           1. Перейти на страницу авторизации
                           2. Авторизоваться
                           3. Собрать и заказать бургер
                           4. Перейти в личный кабинет
                           5. Найти последний заказ и получить номер
                           6. Перейти в ленту заказов
                           ОР: На странице отображен заказ с полученным номером
                           Постусловие: тестовый пользователь удален"''')
    def test_order_number_in_histiry_and_queue(self, driver, new_user):
        auth_page = AuthorizePage(driver)
        auth_page.get_auth_url()
        auth_page.authorization(new_user[0])
        main_page = MainPage(driver)
        main_page.order_burger()
        main_page.close_order_window()
        main_page.click_on_personal_account()
        auth_page.check_orders_history()
        number = auth_page.last_order_number_from_history_get()
        main_page.click_on_queue_of_orders()
        queue_page = QueuePage(driver)
        order_by_number = queue_page.find_order_in_queue(number)
        assert order_by_number.is_displayed() is True

    @pytest.mark.parametrize('locator', [QueueLocators.TOTAL_OF_ALL_TIME_COUNTER, QueueLocators.TOTAL_OF_TODAY_COUNTER])
    @allure.title('Проверка увеличения счетчиков в ленте заказов')
    @allure.description('''Предусловие: в системе создан пользователь
                           1. Перейти на страницу авторизации
                           2. Авторизоваться
                           3. Перейти на ленту заказов
                           4. Получить значение счетчика
                           5. Собрать и заказать бургер
                           6. Перейти в ленту заказов
                           ОР: Счетчик увеличился
                           Постусловие: тестовый пользователь удален"''')
    def test_counters_afret_order(self, locator, driver, new_user):
        auth_page = AuthorizePage(driver)
        main_page = MainPage(driver)
        auth_page.get_auth_url()
        auth_page.authorization(new_user[0])
        main_page.click_on_queue_of_orders()
        counter = int(main_page.get_elements_text(locator))
        main_page.click_on_constructor()
        main_page.order_burger()
        main_page.close_order_window()
        main_page.click_on_queue_of_orders()
        new_counter = int(main_page.get_elements_text(locator))
        assert new_counter > counter
    

    @allure.title('Проверка наличия заказа в статусе "В работе"')
    @allure.description('''Предусловие: в системе создан пользователь
                           1. Перейти на страницу авторизации
                           2. Авторизоваться
                           5. Собрать и заказать бургер
                           6. Перейти в ленту заказов
                           ОР: Номер заказа находится в колонке "В работе"
                           Постусловие: тестовый пользователь удален"''')
    def test_order_in_progress(self, driver, new_user):
        auth_page = AuthorizePage(driver)
        main_page = MainPage(driver)
        auth_page.get_auth_url()
        auth_page.authorization(new_user[0])
        order_number = main_page.order_burger()
        order_number = '0' + order_number
        main_page.close_order_window()
        main_page.click_on_queue_of_orders()
        order_list = main_page.get_elements_text(QueueLocators.IN_PROGRESS_LIST)
        assert order_number in order_list

    