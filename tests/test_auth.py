import allure
from pages.auth_page import AuthPage
from pages.products_page import ProductsPage


@allure.feature("Тестирование модуля авторизации")
class TestAuth:
    @allure.title("Успешная авторизация валидным пользователем")
    def test_successfull_auth(self, page):
        page = AuthPage(page)
        with allure.step("Открываем страницу авторизации"):
            page.open_page('/')
        with allure.step("Авторизовываемся валидным пользователем"):
            page.authorize("standard_user", "secret_sauce")
        with allure.step("Проверяем, что перешли на внутреннюю страницу"):
            page.page.wait_for_url("https://www.saucedemo.com/inventory.html")
            page.wait_for_element_visible(ProductsPage.PRODUCTS_TITLE)

    @allure.title("Неуспешная авторизация невалидным пользователем")
    def test_invalid_user_fail_auth(self, page):
        page = AuthPage(page)
        with allure.step("Открываем страницу авторизации"):
            page.open_page('/')
        with allure.step("Пытаемся авторизоваться невалидным пользователем"):
            page.authorize("testtesttest", "secret_sauce")
        with allure.step("Ждём появления блока с ошибкой"):
            page.wait_for_element_visible(page.INVALID_USER_ERROR_BLOCK)

    @allure.title("Неуспешная авторизация забаненным пользователем")
    def test_banned_user_fail_auth(self, page):
        page = AuthPage(page)
        with allure.step("Открываем страницу авторизации"):
            page.open_page('/')
        with allure.step("Пытаемся авторизоваться забаненным пользователем"):
            page.authorize("locked_out_user", "secret_sauce")
        with allure.step("Ждём появления блока с ошибкой"):
            page.wait_for_element_visible(page.BANNED_USER_ERROR_BLOCK)

    @allure.title("Неуспешная авторизация невалидным пользователем")
    def test_empty_creds_fail_auth(self, page):
        page = AuthPage(page)
        with allure.step("Открываем страницу авторизации"):
            page.open_page('/')
        with allure.step("Пытаемся авторизоваться без указания логина и пароля"):
            page.click(page.LOGIN_BUTTON)
        with allure.step("Ждём появления блока с ошибкой"):
            page.wait_for_element_visible(page.EMPTY_USER_ERROR_BLOCK)

    @allure.title("Неуспешная авторизация пользователем с долгой загрузкой")
    def test_long_load_user_auth(self, page):
        page = AuthPage(page)
        with allure.step("Открываем страницу авторизации"):
            page.open_page('/')
        with allure.step("Авторизовываемся 'долгим' пользователем"):
            page.authorize("performance_glitch_user", "secret_sauce")
        with allure.step("Ждём дольше и проверяем, что перешли на внутреннюю страницу"):
            page.page.wait_for_url("https://www.saucedemo.com/inventory.html")
            page.wait_for_element_visible(ProductsPage.PRODUCTS_TITLE)
