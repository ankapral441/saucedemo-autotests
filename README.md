# saucedemo-test-automation
Автотесты на сайт saucedemo.com

# Инструкция по запуску тестов
## Локальный запуск
1. Установить все зависимости из requirements.txt:

`pip install -r requirements.txt`

2. Установить браузеры для playwright:

`playwright install`

3. Запустить тесты командой

`pytest --alluredir=results -s -v`

4. Запустить страницу с отчётами allure (по желанию)

`allure serve results`


## Запуск в docker-контейнере