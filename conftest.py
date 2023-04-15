from selenium import webdriver
from selenium.webdriver.chrome.options import Options as chromeOptions
from selenium.webdriver.firefox.options import Options as mozzillaOptions
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
import pytest


# ФАЙЛ CONFTEST
# pytest автоматически находит файл с именем conftest и даюи доступ к его содержимому при выполнении тестов
# обычно, в подобно файле хранятся фикстуры


# создание функции для того, чтобы принимать опцию --browser_name в консоли
def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default=None,
                     help='Choose browser: chrome or mozilla (default chrome)')
    parser.addoption('--language', action='store', default='en',
                     help='Choose language: en(gb)/ru/ko... (default en)')


# пример фикстуры
# @pytest.fixture  # декоратор обозначающий, что тут объявлена фикстура
# def browser_fixture_test():
#     print("\nstart browser for test... AUTOUSE=FALSE, SCOPE_DEAFAULT")
#     browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
#     return browser  # эту фикстуру можно передавать в функцию как аргумент, чтобы сразу получать доступ к браузеру


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

# фикстура для создания браузера
@pytest.fixture
def browser(request):
    # это выполнится перед указанном в scope периоде
    language = request.config.getoption('language')
    browser_name = request.config.getoption('browser_name')  # получаю параметр browser_name

    if browser_name == 'chrome':
        print(f"\nStart chrome browser with language {language} for test...")
        options_chrome = chromeOptions()
        options_chrome.add_experimental_option('prefs', {'intl.accept_languages': language})
        browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options_chrome)

    elif browser_name == 'mozilla':
        options_firefox = mozzillaOptions()
        options_firefox.set_preference('intl.accept_languages', language)
        print(f"\nStart mozilla browser for test with language {language}...")
        browser = webdriver.Firefox(service=Service(GeckoDriverManager().install()), options=options_firefox)

    else:
        options_chrome = chromeOptions()
        options_chrome.add_experimental_option('prefs', {'intl.accept_languages': language})
        print(f'\nChosen browser not available. Available browser names: mozilla/chrome')
        print(f"\nStart chrome browser for test BY DEFAULT with language {language}...")
        browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options_chrome)

    yield browser  # статья на хабре про yield https://habr.com/ru/post/132554/

    # этот код выполнится после завершения указанного периода в scope
    print("\nquit chrome browser..")
    browser.quit()


# фикстура для создания браузера mozilla
# @pytest.fixture()
# def browser_mozilla():
#     # это выполнится перед указанном в scope периоде
#     print("\nStart mozilla browser for test...")
#     browser = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
#     yield browser  # статья на хабри про yield https://habr.com/ru/post/132554/
#     # этот код выполнится после завершения указанного периода в scope
#     print("\nquit mozilla browser..")
#     browser.quit()

# фикстура для создания браузера chrome
# @pytest.fixture()
# def browser_mozilla():
#     # это выполнится перед указанном в scope периоде
#     print("\nStart chrome browser for test...")
#     browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
#     yield browser  # статья на хабри про yield https://habr.com/ru/post/132554/
#     # этот код выполнится после завершения указанного периода в scope
#     print("\nquit chrome browser..")
#     browser.quit()


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
