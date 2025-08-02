import allure
from pages.base_page import BasePage

from data import *
from locators.auth_page_locators import AuthPageLocators

class AuthorizePage(BasePage):

    @allure.step("Переход по url")
    def get_auth_url(self):
        self.driver.get(Urls.AUTH_PAGE)

    @allure.step('Клик по ссылке "Восстановить пароль"')
    def click_restore_password_and_get_title(self):
        self.wait_for_visibiliti_of_element(AuthPageLocators.RESTORE_PASSWORD_LINK)
        self.wait_for_and_click_element(AuthPageLocators.RESTORE_PASSWORD_LINK)
        self.wait_for_visibiliti_of_element(AuthPageLocators.EMAIL_FIELD)
        title_element = self.get_elements_text(AuthPageLocators.RESTORE_TITLE)
        return title_element

    @allure.step('Заполнить email и кликнуть Восстановить пароль')
    def restore_password(self, email):
        self.click_restore_password_and_get_title()
        self.send_keys(AuthPageLocators.EMAIL_FIELD, email)
        self.wait_for_and_click_element(AuthPageLocators.RESTORE_BUTTON)
        restore_code_text = self.get_elements_text(AuthPageLocators.CODE_FIELD)
        return restore_code_text
    
    @allure.step('Проверить заголовок страницы авторизации')
    def check_login_page(self):
        return self.get_elements_text(AuthPageLocators.RESTORE_TITLE)
    
    @allure.step('Проверить раздел Профиль в личном кабинете')
    def check_profile_page(self):
        return self.get_elements_text(AuthPageLocators.PRIFILE_TITLE)
    
    @allure.step('Авторизация')
    def authorization(self, user_data):
        email, password = user_data.get('email'), user_data.get('password')
        self.send_keys(AuthPageLocators.EMAIL_FIELD, email)
        self.send_keys(AuthPageLocators.PASSWORD_FIELD, password)
        self.wait_for_and_click_element(AuthPageLocators.LOGIN_BUTTON)

    @allure.step('Проверить видимость поля Пароль')
    def visibility_of_password_field(self):
        self.wait_for_visibiliti_of_element(AuthPageLocators.PASSWORD_FIELD)
        self.click_on_element_for_firefox(AuthPageLocators.EYE_ICON_PASSWORD)
        if self.wait_for_visibiliti_of_element(AuthPageLocators.PASSWORD_VISIBLE_FIELD):
            return True
        
    @allure.step('Проверить вкладку История заказов')
    def check_orders_history(self):
        self.wait_for_and_click_element(AuthPageLocators.ORDERS_HISTORY)
        element = self.wait_for_visibiliti_of_element(AuthPageLocators.ORDERS_HISTORY)
        element_class = element.get_attribute("class")
        return element_class == ORDER_HISTORY_ACTIVE
    
    @allure.step('Выйти из аккаунта')
    def logout(self):
        self.wait_for_and_click_element(AuthPageLocators.LOGOUT_BUTTON)
        return self.check_login_page()
    
    @allure.step('Получить номер последнего заказа из истории')
    def last_order_number_from_history_get(self):
        return self.get_elements_text(AuthPageLocators.LAST_ORDER_IN_HISTORY)
        
    