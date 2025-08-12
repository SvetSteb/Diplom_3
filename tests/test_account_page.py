import allure 

from data import *
from pages.auth_page import AuthorizePage
from pages.main_page import MainPage

@allure.feature("Тестирование функционала личного кабинета пользователя")
class TestAccountPage:

   @allure.title('Проверка перехода с главной страницы в Личный кабинет для авторизованного пользователя')
   @allure.description('''Предусловие: в системе создан новый тестовый пользователь
                           1. Перейти на главную страницу
                           2. Клик по кнопке Личный кабинет
                           3. Авторизоваться
                           4. Вернуться в личный кабинет по кнопке Личный кабинет
                           ОР: На странице отображен раздел "Профиль"
                           Постусловие: удалить тестого пользователя"''')
   def test_personal_account_for_auth_user(self, driver,new_user):
       driver.get(Urls.MAIN_PAGE)
       main_page = MainPage(driver)
       main_page.click_on_personal_account()
       auth_page = AuthorizePage(driver)
       auth_page.authorization(new_user[0])
       main_page.click_on_personal_account()
       assert auth_page.check_profile_page() == "Профиль" 

   @allure.title('Переход в раздел «История заказов»')
   @allure.description('''Предусловие: в системе создан новый тестовый пользователь
                           1. Перейти на главную страницу
                           2. Клик по кнопке Личный кабинет
                           3. Авторизоваться
                           4. Вернуться в личный кабинет по кнопке Личный кабинет
                           5. Перейти в раздел "История заказов"
                           ОР: Название раздела "История заказов" активно
                           Постусловие: удалить тестого пользователя"''')
   def test_personal_account_order_history(self, driver,new_user):
       driver.get(Urls.MAIN_PAGE)
       main_page = MainPage(driver)
       main_page.click_on_personal_account()
       auth_page = AuthorizePage(driver)
       auth_page.authorization(new_user[0])
       main_page.click_on_personal_account()
       assert auth_page.check_orders_history()

   @allure.title('Проверка выхода из аккаунта')
   @allure.description('''Предусловие: в системе создан новый тестовый пользователь
                           1. Перейти на главную страницу
                           2. Клик по кнопке Личный кабинет
                           3. Авторизоваться
                           4. Вернуться в личный кабинет по кнопке Личный кабинет
                           5. Клик на "Выход"
                           ОР: Переход на страницу авторизации
                           Постусловие: удалить тестого пользователя"''')
   def test_logout_user(self, driver,new_user):
       driver.get(Urls.MAIN_PAGE)
       main_page = MainPage(driver)
       main_page.click_on_personal_account()
       auth_page = AuthorizePage(driver)
       auth_page.authorization(new_user[0])
       main_page.click_on_personal_account()
       logout = auth_page.logout()
       assert logout == "Вход"
