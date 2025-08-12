import allure 

from data import *


@allure.feature("Тестирование функции восстановления пароля")
class TestRestorePassword:

    @allure.title('Переход на страницу восстановления пароля по кнопке «Восстановить пароль»')
    @allure.description('''1. Перейти на страницу авторизации
                           2. Клик по ссылке "Восстановить пароль"
                           ОР: На странице отображен заголовок "Восстановление пароля"''')
    def test_restore_password_get_restore_page(self, auth_page):
        title = auth_page.click_restore_password_and_get_title()
        assert title == "Восстановление пароля"


    @allure.title('Восстановление пароля: клик по кнопке Восстановить')
    @allure.description('''Предусловие: в системе создан пользователь
                           1. Перейти на страницу авторизации
                           2. Клик по ссылке "Восстановить пароль"
                           3. Заполнить поле EMAIL
                           4. Клик о кнопке Восстановить
                           ОР: На странице отображен текст "Введите код из письма
                           Постусловие: тестовый пользователь удален"''')
    def test_restore_password(self, auth_page, new_user):
        email = new_user[0].get('email')
        restore_code_text = auth_page.restore_password(email)
        assert restore_code_text == 'Введите код из письма'


    @allure.title('Клик по кнопке показать/скрыть пароль делает поле активным — подсвечивает его')
    @allure.description('''1. Перейти на страницу авторизации
                           2. Клик по иконке видимости содержимого поля (глаз)
                           ОР: Локатор поля изменился"''')
    def test_visibility_of_password_field(self, auth_page):
        assert auth_page.visibility_of_password_field()
