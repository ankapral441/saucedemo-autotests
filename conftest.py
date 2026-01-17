import pytest
from playwright.sync_api import sync_playwright


def pytest_addoption(parser):
    # добавляем возможность скрывать наш браузер при передача флага --hide
    parser.addoption(
        "--hide",
        action="store_true",
        default=False
    )


@pytest.fixture
def playwright():
    with sync_playwright() as playwright:
        yield playwright


@pytest.fixture
def browser(playwright, request):
    hide = request.config.getoption("--hide")
    browser = playwright.chromium.launch(headless=hide)  # запускаем браузер хром
    yield browser  # передаём браузер на время выполнения теста
    browser.close()  # не забываем закрыть браузер после теста


@pytest.fixture
def page(browser):
    page = browser.new_page()  # создаём страницу в нашем браузере
    yield page  # передаём страницу в тест