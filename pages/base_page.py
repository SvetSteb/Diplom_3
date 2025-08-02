import allure
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains

class BasePage:

    @allure.step('Получить и инициализировать драйвер')
    def __init__(self, driver):
        self.driver = driver


    @allure.step('Ожидание и получение элемента')
    def wait_for_visibiliti_of_element(self, locator):
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(locator))
        return self.driver.find_element(*locator)
    

    @allure.step('Ожидание кликабельности, клик по элементу')
    def wait_for_and_click_element(self, locator):
        WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(locator))
        browser = self.driver.name.lower()
        if browser == 'firefox':
            self.click_on_element_for_firefox(locator)
        else:
            self.driver.find_element(*locator).click()

    @allure.step('Клик по элементу')
    def click_for_button_under_modal(self, locator):
        WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(locator))
        browser = self.driver.name.lower()
        if browser == 'firefox':
            self.scroll_and_click_on__button(locator)
        else:
            self.driver.find_element(*locator).click()


    @allure.step('Получение текста элемента')
    def get_elements_text(self, locator):
        text = self.wait_for_visibiliti_of_element(locator).text
        return text


    @allure.step('Прокрутить страницу до элемента')
    def scroll_to_element(self, locator):
        element = self.wait_for_visibiliti_of_element(locator)
        try:
            actions = ActionChains(self.driver)
            actions.move_to_element(element).perform()
        except:
            self.driver.execute_script("arguments[0].scrollIntoView();", element)


    @allure.step('Прокрутить до элемента и кликнуть')
    def scroll_and_click_on__button(self, locator):
        element = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(locator))
        self.scroll_to_element(locator)
        try:
            element.click()
        except:
            self.driver.execute_script("arguments[0].click();", element)


    @allure.step('Заполнение поля данными')
    def send_keys(self, locator, text):
        self.wait_for_visibiliti_of_element(locator).send_keys(text)


    @allure.step('Клик на элемент, закрытый модальным окном')
    def click_on_element_for_firefox(self, locator):
        element = self.driver.find_element(*locator)
        ActionChains(self.driver).move_to_element(element).click().perform()

    def drag_and_drop_for_chrome(self, from_locator, to_locator):
        element_from = self.wait_for_visibiliti_of_element(from_locator)
        element_to = self.wait_for_visibiliti_of_element(to_locator)
        actions = ActionChains(self.driver)
        actions.drag_and_drop(element_from, element_to).perform()

    def drag_and_drop_for_firefox(self, locator_from, locator_to):
        self.wait_for_visibiliti_of_element(locator_from)
        self.wait_for_visibiliti_of_element(locator_to)
        element_from = self.driver.find_element(*locator_from)
        element_to = self.driver.find_element(*locator_to)
        self.driver.execute_script("""
                   var source = arguments[0];
                   var target = arguments[1];
                   var evt = document.createEvent("DragEvent");
                   evt.initMouseEvent("dragstart", true, true, window, 0, 0, 0, 0, 0, false, false, false, false, 0, null);
                   source.dispatchEvent(evt);
                   evt = document.createEvent("DragEvent");
evt.initMouseEvent("dragenter", true, true, window, 0, 0, 0, 0, 0, false, false, false, false, 0, null);
                   target.dispatchEvent(evt);
                   evt = document.createEvent("DragEvent");
                   evt.initMouseEvent("dragover", true, true, window, 0, 0, 0, 0, 0, false, false, false, false, 0, null);
                   target.dispatchEvent(evt);
                   evt = document.createEvent("DragEvent");
                   evt.initMouseEvent("drop", true, true, window, 0, 0, 0, 0, 0, false, false, false, false, 0, null);
                   target.dispatchEvent(evt);
                   evt = document.createEvent("DragEvent");
                   evt.initMouseEvent("dragend", true, true, window, 0, 0, 0, 0, 0, false, false, false, false, 0, null);
                   source.dispatchEvent(evt);
               """, element_from, element_to)

    @allure.step('Перетащить объект')
    def drag_and_drop(self, locator_from, locator_to):
        browser = self.driver.name.lower()
        if browser == 'firefox':
            self.drag_and_drop_for_firefox(locator_from, locator_to)
        else:
            self.drag_and_drop_for_chrome(locator_from, locator_to)

    @allure.step('Ожидание смены текста в элементе')
    def wait_until_text_changed(self, locator, initial_text):
        def predicate(driver):
            try:
                current = driver.find_element(*locator).text
                return current != initial_text
            except:
                return False
        return predicate 
    
    @allure.step('Ожидание исчезновения элемента')
    def wait_for_invisibility(self, locator):
        WebDriverWait(self.driver, 10).until(EC.invisibility_of_element(locator))

    @allure.step('Ожидание нового текста в элементе')
    def wait_new_text(self, locator, text):
        WebDriverWait(self.driver, 15).until(self.wait_until_text_changed(locator, text))
