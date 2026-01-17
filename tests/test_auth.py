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
