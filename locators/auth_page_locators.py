from selenium.webdriver.common.by import By


class AuthPageLocators:
    EMAIL_FIELD = (By.XPATH, './/input[@class="text input__textfield text_type_main-default" and @name="name"]') # Поле Емаейл
    PASSWORD_FIELD = (By.XPATH, './/input[@class="text input__textfield text_type_main-default" and @name="Пароль"]') # Поле пароль
    EYE_ICON_PASSWORD = (By.XPATH, './/div[contains(@class,"icon-action")]')
    PASSWORD_VISIBLE_FIELD = (By.XPATH, './/div/input[@class="text input__textfield text_type_main-default" and @type = "text"]')
    LOGIN_BUTTON = (By.XPATH, './/button[@class="button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa" and text()="Войти"]') # Кнопка Войти
    RESTORE_PASSWORD_LINK = (By.XPATH, './/a[@class="Auth_link__1fOlj" and text()="Восстановить пароль"]') # ссылка Восстановить пароль
    RESTORE_BUTTON = (By.XPATH, './/button[@class="button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa" and text()="Восстановить"]') # 
    CODE_FIELD = (By.XPATH, './/div[@class="input pr-6 pl-6 input_type_text input_size_default"]/label[@class="input__placeholder text noselect text_type_main-default"]')
    RESTORE_TITLE = (By.XPATH, './/div[@class="Auth_login__3hAey"]/h2')
    OVERLAY_BUNNER = (By.XPATH, './/div[@class="Modal_modal_overlay__x2ZCr"]')
    PRIFILE_TITLE = (By.XPATH, './/a[@href="/account/profile"]')
    ORDERS_HISTORY = (By.XPATH, './/a[@href="/account/order-history"]')

    LOGOUT_BUTTON = (By.XPATH, './/button[text()="Выход"]')

    LAST_ORDER_IN_HISTORY = (By.XPATH, './/ul[@class="OrderHistory_profileList__374GU OrderHistory_list__KcLDB"]/li[last()]/a/div/p[@class="text text_type_digits-default"]')