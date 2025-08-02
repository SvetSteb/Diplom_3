import allure
from pages.base_page import BasePage
from selenium.webdriver.common.by import By

from data import *
from locators.queue_page_locators import QueueLocators
from helpers import format_locator_for_order_number, format_locator_for_order_long_number

class QueuePage(BasePage):
    
    @allure.step('Клик на заказ в ленте')
    def click_on_order_info(self):
        self.wait_for_and_click_element(QueueLocators.FIRST_ORDER_IN_QUEUE)
        return self.wait_for_visibiliti_of_element(QueueLocators.ORDER_INFO_WINDOW)
    
    @allure.step('Найти заказ в ленте по номеру')
    def find_order_in_queue(self, number):
        locator = format_locator_for_order_long_number(number)
        return self.wait_for_visibiliti_of_element(locator)

    @allure.step('Получить число заказов из счетчика по локатору')
    def get_counter_of_orders(self, locator):
        return self.get_elements_text(locator)
    
    