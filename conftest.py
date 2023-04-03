from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import pytest


# ФАЙЛ CONFTEST
# pytest автоматически находит файл с именем conftest и даюи доступ к его содержимому при выполнении тестов
# обычно, в подобно файле хранятся фикстуры


# пример фикстуры
@pytest.fixture  # декоратор обозначающий, что тут объявлена фикстура
def browser1():
    print("\nstart browser for test... AUTOUSE=FALSE, SCOPE_DEAFAULT")
    browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    return browser  # эту фикстуру можно передавать в функцию как аргумент, чтобы сразу получать доступ к браузеру


# пример фикстуры с yield
# scope может принимать:
# “session” - выполнения фикстуры для каждой сессии,
# “module” - выполнения фикстуры каждого модуля
# “class” - выполнения фикстуры каждого класс
# “function” - выполнения фикстуры каждого класс (по умолчанию)

# autouse=True - запускает фикстуру с указанной в scope периодичностью автоматически, фикстуру не нужно вызывать (передавать как аргумент)

# все, что идет до yield - setup (выполнится ДО начала периода указанного в scope)
# все, что после - teardown (выполнится ПОСЛЕ периода указанного в scope)

# то есть при scope=function будет выполняться указанный setup и teardown для каждой функции
@pytest.fixture()
def browser():
    # это выполнится перед указанном в scope периоде
    print("\nstart browser for test...")
    browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    yield browser  # статья на хабри про yield https://habr.com/ru/post/132554/
    # этот код выполнится после завершения указанного периода в scope
    print("\nquit browser..")
    browser.quit()


# для авторизации на степик
def stepik_auth(browser):
    auth_btn = browser.find_element(By.CSS_SELECTOR, '.navbar__auth.navbar__auth_login')

    auth_link = auth_btn.get_attribute('href')

    browser.get(auth_link)

    email_login_form = browser.find_element(By.CSS_SELECTOR, '#id_login_email')
    password_login_form = browser.find_element(By.CSS_SELECTOR, '#id_login_password')

    email_login_form.send_keys('arkoah072@gmail.com')
    password_login_form.send_keys('weiterbildung2000')

    submit_login_form_btn = browser.find_element(By.CSS_SELECTOR, '.sign-form__btn')
    submit_login_form_btn.click()
