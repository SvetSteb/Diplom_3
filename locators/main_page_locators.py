from selenium.webdriver.common.by import By

class MainPageLocators:

    PERSONAL_ACCOUNT_BUTTON = (By.XPATH, './/*[text()="Личный Кабинет"]') #кнопка Личный кабинет
    OVERLAY = (By.XPATH, './/div[@class="Modal_modal_overlay__x2ZCr"]')
    CONSTRUCTOR = (By.XPATH, './/p[text()="Конструктор"]')
    QUEUE = (By.XPATH, './/p[@class="AppHeader_header__linkText__3q_va ml-2" and text()="Лента Заказов"]')
    QUEUE_TITLE = (By.XPATH, './/h1[@class="text text_type_main-large mt-10 mb-5"]')
    CONSTRUCTOR_TITLE = (By.XPATH, './/h1[@class = "text text_type_main-large mb-5 mt-10"]')
    BASCET = (By.XPATH, './/ul[@class="BurgerConstructor_basket__list__l9dp_"]')
    BUN_1 = (By.XPATH, './/a[@href="/ingredient/61c0c5a71d1f82001bdaaa6d"]')
    BUN_TITLE_MODAL = (By.XPATH, './/h2[@class="Modal_modal__title_modified__3Hjkd Modal_modal__title__2L34m text text_type_main-large pl-10"]')
    CLOSE_MODAL_WINDOW = (By.XPATH, './/button[@class="Modal_modal__close_modified__3V5XS Modal_modal__close__TnseK"]')
    SAUSE_1 = (By.XPATH, './/a[@href="/ingredient/61c0c5a71d1f82001bdaaa73"]')
    ORDER_BUTTON = (By.XPATH, './/button[text()="Оформить заказ"]')
    ODER_MODAL_WINDOW = (By.CLASS_NAME, 'Modal_modal__contentBox__sCy8X pt-30 pb-30')
    CLOSE_ORDER_WINDOW = (By.XPATH, './/button[@class="Modal_modal__close_modified__3V5XS Modal_modal__close__TnseK"]')
    ORDER_NUMBER = (By.XPATH, './/h2[@class="Modal_modal__title_shadow__3ikwq Modal_modal__title__2L34m text text_type_digits-large mb-8"]')

