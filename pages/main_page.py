import allure

from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators
from helpers import *


class MainPage(BasePage):

    @allure.step('Клик по кнопке "Личный кабинет"')
    def click_on_personal_account(self):
        self.click_for_button_under_modal(MainPageLocators.PERSONAL_ACCOUNT_BUTTON)

    @allure.step('Клик по кнопке "Лента заказов"')
    def click_on_queue_of_orders(self):
        self.click_for_button_under_modal(MainPageLocators.QUEUE)

    @allure.step('Клик по кнопке "Конструктор"')
    def click_on_constructor(self):
        self.wait_for_and_click_element(MainPageLocators.CONSTRUCTOR)
    
    @allure.step('Перетащить один ингредиент в "бургер"(корзину)')
    def put_one_ingredient(self, ingredient_locator):
        self.drag_and_drop(ingredient_locator, MainPageLocators.BASCET)
        counter_locator = format_locator_for_counter(ingredient_locator)
        counter = self.wait_for_visibiliti_of_element(counter_locator)
        return counter.text
    
    @allure.step('Собрать бургер, нажать Заказать')
    def order_burger(self):
        self.drag_and_drop(MainPageLocators.BUN_1, MainPageLocators.BASCET)
        self.drag_and_drop(MainPageLocators.SAUSE_1, MainPageLocators.BASCET)
        self.wait_for_and_click_element(MainPageLocators.ORDER_BUTTON)
        self.wait_for_visibiliti_of_element(MainPageLocators.ORDER_NUMBER)
        self.wait_new_text(MainPageLocators.ORDER_NUMBER, '9999')
        number_element = self.get_elements_text(MainPageLocators.ORDER_NUMBER)
        return number_element
    
    @allure.step('Клик на ингредиент(булка), получить модальное окно с информацией')
    def click_on_ingredient(self):    
        self.wait_for_and_click_element(MainPageLocators.BUN_1)
        modal_window_title = self.wait_for_visibiliti_of_element(MainPageLocators.BUN_TITLE_MODAL)
        return modal_window_title
    
    @allure.step('Закрыть модельное окно c инфо об ИНГРЕДИЕНТЕ по крестику')
    def close_modal_window(self):    
        self.wait_for_and_click_element(MainPageLocators.CLOSE_MODAL_WINDOW)
        self.wait_for_invisibility(MainPageLocators.CLOSE_MODAL_WINDOW)
        
    @allure.step('Закрыть модельное окно c инфо о ЗАКАЗЕ по крестику')
    def close_order_window(self):    
        self.wait_for_and_click_element(MainPageLocators.CLOSE_ORDER_WINDOW)
        