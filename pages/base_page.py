import allure
from playwright.sync_api import Page


class BasePage:
    def __init__(self, page: Page, base_url = "https://www.saucedemo.com"):
        self.page = page
        self.base_url = base_url

    def open_page(self, url):
        with allure.step(f"Открываем страницу по урлу {self.base_url + url}"):
            self.page.goto(url=self.base_url + url)

    def click(self, selector):
        with allure.step("Кликаем по элементу"):
            self.page.click(selector)

    def wait_for_element_visible(self, selector, timeout = None):
        with allure.step("Дожидаемся элемента"):
            self.page.wait_for_selector(selector=selector, timeout=timeout)