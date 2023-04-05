from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
# импортируем класс By, который позволяет выбрать способ поиска элемента
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from conftest import stepik_auth
import time
import os
import unittest
import pytest


# ===========================================
# УСТАНОВКА АКТУАЛЬНОЙ ВЕРСИИ ХРОМ ДРАЙВЕРА
def get_actual_browser():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))


# ===========================================


# ===========================================
# ПРИМЕР РАБОТЫ С САЙТОМ
def work_with_browser():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    # Метод get сообщает браузеру, что нужно открыть сайт по указанной ссылке
    driver.get("https://suninjuly.github.io/text_input_task.html")
    time.sleep(5)

    # Метод find_element позволяет найти нужный элемент на сайте, указав путь к нему. Способы поиска элементов мы обсудим позже
    # Метод принимает в качестве аргументов способ поиска и значение, по которому мы будем искать
    # Ищем поле для ввода текста
    textarea = driver.find_element(By.CSS_SELECTOR, ".textarea")

    # Напишем текст ответа в найденное поле
    textarea.send_keys("get()")
    time.sleep(5)

    # Найдем кнопку, которая отправляет введенное решение
    submit_button = driver.find_element(By.CSS_SELECTOR, ".submit-submission")

    # Скажем драйверу, что нужно нажать на кнопку. После этой команды мы должны увидеть сообщение о правильном ответе
    submit_button.click()
    time.sleep(5)

    # После выполнения всех действий мы должны не забыть закрыть окно браузера
    driver.quit()


# =========================================


# =========================================
# Для закрытия браузера в конце программы, даже если в течении программы возникла ошибка можно использовать конструкции:
def open_browser():
    with webdriver.Chrome(service=Service(ChromeDriverManager().install())) as browser:
        browser.get('https://google.com')

    try:
        browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        browser.get('https://google.com')
    finally:
        browser.quit()


# ==========================================


# ==========================================
# 1.6 шаг 4
# Заполнить формы и получить проверочный код, который будет ответом
def step_1_6_4():
    with webdriver.Chrome(service=Service(ChromeDriverManager().install())) as browser:
        browser.get('http://suninjuly.github.io/simple_form_find_task.html')
        first_name_form = browser.find_element(By.CSS_SELECTOR, '[name="first_name"]')
        first_name_form.send_keys('Arseniy')
        last_name_form = browser.find_element(By.CSS_SELECTOR, '[name="last_name"]')
        last_name_form.send_keys('Kosolapov')
        city_form = browser.find_element(By.CSS_SELECTOR, '.form-control.city')
        city_form.send_keys('Tyumen')
        country_form = browser.find_element(By.ID, "country")
        country_form.send_keys('Russia')
        submit_btn = browser.find_element(By.ID, "submit_button")
        submit_btn.click()
        time.sleep(5)


# step_1_6_4()
# ==================================================


# ==================================================
# 1.6 шаг 5
# Найти нужную ссылку, перейти по ней и заполнить форму
import math


def step_1_6_5():
    with webdriver.Chrome(service=Service(ChromeDriverManager().install())) as browser:
        browser.get('http://suninjuly.github.io/find_link_text')
        browser.find_element(By.PARTIAL_LINK_TEXT, str(math.ceil(math.pow(math.pi, math.e) * 10000))).click()
        first_name_form = browser.find_element(By.CSS_SELECTOR, '[name="first_name"]')
        first_name_form.send_keys('Arseniy')
        last_name_form = browser.find_element(By.CSS_SELECTOR, '[name="last_name"]')
        last_name_form.send_keys('Kosolapov')
        city_form = browser.find_element(By.CSS_SELECTOR, '.form-control.city')
        city_form.send_keys('Tyumen')
        country_form = browser.find_element(By.ID, 'country')
        country_form.send_keys('Russia')
        submit_btn = browser.find_element(By.CSS_SELECTOR, 'button.btn')
        submit_btn.click()
        time.sleep(5)


# step_1_6_5()
# ===================================================


# ===================================================
# пример подтверждения ввода (нажать Enter) без клика
from selenium.webdriver.common.keys import Keys


def press_enter_without_click():
    with webdriver.Chrome(service=Service(ChromeDriverManager().install())) as browser:
        browser.get("https://google.com")
        input_form = browser.find_element(By.CSS_SELECTOR, "input.gLFyf")
        input_form.send_keys("test")

        browser.get("https://google.com")
        input_form = browser.find_element(By.CSS_SELECTOR, "input.gLFyf")
        input_form.send_keys("test")
        # Разные возможности подтвердить ввод (нажать ENTER)
        input_form.send_keys(Keys.RETURN)
        input_form.send_keys(Keys.ENTER)
        input_form.submit()


# test_press_enter_without_click()
# ===================================================


# ===================================================
# 1.6 шаг 7
# Заполнить форму из 100 полей и получить ответ, нажав кнопку подтверждения
def step_1_6_7():
    with webdriver.Chrome(service=Service(ChromeDriverManager().install())) as browser:
        browser.get("http://suninjuly.github.io/huge_form.html")
        input_forms = browser.find_elements(By.CSS_SELECTOR, ".first_block > input")
        for form in input_forms:
            form.send_keys('bebra')
        browser.find_element(By.CSS_SELECTOR, ".btn").click()
        time.sleep(5)


# step_1_6_7()
# ===================================================


# ==========================================
# 1.6 шаг 8
# Заполнить формы и получить проверочный код, который будет ответом
def step_1_6_8():
    with webdriver.Chrome(service=Service(ChromeDriverManager().install())) as browser:
        browser.get('http://suninjuly.github.io/find_xpath_form')

        first_name_form = browser.find_element(By.CSS_SELECTOR, 'input[name="first_name"]')
        first_name_form.send_keys('Arseniy')

        last_name_form = browser.find_element(By.CSS_SELECTOR, 'input[name="last_name"]')
        last_name_form.send_keys('Kosolapov')

        city_form = browser.find_element(By.CSS_SELECTOR, '.form-control.city')
        city_form.send_keys('Tyumen')

        country_form = browser.find_element(By.ID, "country")
        country_form.send_keys('Russia')

        submit_btn = browser.find_element(By.XPATH, '//form[@action="#"]/*/button[contains(text(), "Submit")]')
        submit_btn.click()
        time.sleep(5)


# step_1_6_8()
# ==================================================


# ==========================================
# 1.6 шаг 10
# Заполнить форму регистрации
def step_1_6_10():
    with webdriver.Chrome(service=Service(ChromeDriverManager().install())) as browser:
        browser.get('http://suninjuly.github.io/registration2.html')

        select_values = {1: 'first', 2: 'second', 3: 'third'}
        required_values = ['Arseniy', 'Kosolapov', 'hllwwrld@gmail.com']

        required_forms = [browser.find_element(By.CSS_SELECTOR, f'.first_block input.form-control.{select_values[i]}')
                          for i in range(1, 4)]
        for i in range(len(required_forms)):
            required_forms[i].send_keys(required_values[i])

        time.sleep(3)

        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()

        time.sleep(1)

        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        welcome_text = welcome_text_elt.text

        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        assert "Congratulations! You have successfully registered!" == welcome_text


# step_1_6_10()
# ==================================================


# ====================================================
# 2.1 шаг 5
# найди значение на странице, вычислить по формуле другое значение
# вставить значение на страницу
# проставить чек-бокс и радио-кнопку
# отправить форму


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


def step_2_1_5():
    # получаем актуальную версию драйвера и открываем браузер
    with webdriver.Chrome(service=Service(ChromeDriverManager().install())) as browser:
        browser.get('https://suninjuly.github.io/math.html')
        x_elem = browser.find_element(By.ID, 'input_value')
        x = int(x_elem.text)

        input_form = browser.find_element(By.ID, 'answer')
        input_form.send_keys(calc(x))

        robot_checkbox = browser.find_element(By.ID, 'robotCheckbox')
        robot_checkbox.click()

        robot_radiobtn = browser.find_element(By.ID, "robotsRule")
        robot_radiobtn.click()

        fin = browser.find_element(By.CLASS_NAME, "btn")
        fin.click()

        time.sleep(5)


# step_2_1_5()
# ====================================================


# ====================================================
# 2.1 шаг 7
# найти значение атрибута определенной картинки на странице
# на основании полученного значение вычислить другое
# ввести его на странице
# выбрать чекбокс
# выбрать радио-кнопку
# отправить форму


def step_2_1_7():
    with webdriver.Chrome(service=Service(ChromeDriverManager().install())) as browser:
        browser.get('http://suninjuly.github.io/get_attribute.html')
        treasure_elem = browser.find_element(By.ID, 'treasure')
        treasure_value = calc(int(treasure_elem.get_attribute("valuex")))

        input_form = browser.find_element(By.ID, 'answer')
        input_form.send_keys(treasure_value)

        robot_checkbox = browser.find_element(By.ID, 'robotCheckbox')
        robot_checkbox.click()

        robot_radiobtn = browser.find_element(By.ID, "robotsRule")
        robot_radiobtn.click()

        fin = browser.find_element(By.CLASS_NAME, "btn")
        fin.click()

        time.sleep(5)


# step_2_1_7()
# ====================================================


# =====================================================
# 2.1 шаг 8
# в выпадающем списке значения не имеют никаких атриубтов, все значения обозначаются тэгом option
# пример, как выбрать в таком списке второе значение

# browser.find_element(By.TAG_NAME, "select").click()
# browser.find_element(By.CSS_SELECTOR, "option:nth-child(2)").click()

# либо

# =====================================================


# =====================================================
from functools import reduce


# 2.2 шаг 3
# открыть страницу;
# считать два числа и;
# выбрать в выпадающем списке их сумму;
# отправить форму
def step_2_2_3():
    with webdriver.Chrome(service=Service(ChromeDriverManager().install())) as browser:
        browser.get('http://suninjuly.github.io/selects1.html')

        to_sum_elem = browser.find_elements(By.CSS_SELECTOR, 'h2 > [id*="num"]')
        summed_red = reduce(lambda start, elem: int(elem.text) + start, to_sum_elem, 0)

        # тоже самое, что и summed_red, только в две строки и другими инструментами
        # to_sum_values = list(map(lambda lst: int(lst.text), to_sum_elem))
        # summed_sum = sum(to_sum_values)

        # вариант 1 - как я реализовал изначально - через создания списка значений выпад. списка и поиска в нем подхоядщего
        # dropdown_elem = browser.find_element(By.ID, 'dropdown')
        # dropdown_elem.click()
        #
        # dropdown_elements = browser.find_elements(By.CSS_SELECTOR, '#dropdown > option')
        #
        # for elem in dropdown_elements:
        #     if elem.text.isdigit():
        #         if int(elem.text) == summed_red:  # или summmed_sum
        #             answer = browser.find_element(By.CSS_SELECTOR, f'#dropdown > option:nth-child({dropdown_elements.index(elem) + 1})')
        #             answer.click()
        #             break

        # вариант 2
        # более удобный, с Select
        # в функцию Select передается web-элемент список, далее можно обращаться к любому элементу этого списка
        dropdown_values = Select(browser.find_element(By.CSS_SELECTOR, '#dropdown'))

        # далее обращаюся к списку значений и ищу в нем нудную мне сумму
        # найденная сумма автоматически выбирается (происходит клик)
        dropdown_values.select_by_visible_text(str(summed_red))

        # dropdown_values.select_by_value(str(summed_red))  # так-же можно искать по атриубуту value
        # dropdown_values.select_by_index()  # или по индексу самого значения в списке элементов выпадающего списка

        time.sleep(1)

        btn = browser.find_element(By.CSS_SELECTOR, ".btn")
        btn.click()

        time.sleep(5)


# step_2_2_3()
# =====================================================


# =====================================================
# Открыть страницу
# найти x
# ввести значение, посчитанное на основании икс в форму
# сделать так, чтобы можно было нажать чек бокс, радиокнопку и нажать submit
def step_2_2_6():
    with webdriver.Chrome(service=Service(ChromeDriverManager().install())) as browser:
        browser.get('http://suninjuly.github.io/execute_script.html')
        # нахожу x и перевожу его в int
        x_elem = browser.find_element(By.ID, 'input_value')
        x = int(x_elem.text)

        # нахожу форму для ввода посчитанного значения по x, заполняю форму
        input_form = browser.find_element(By.ID, 'answer')
        input_form.send_keys(calc(x))

        # нахожу элемент-кнопку, проматываю страницу, чтобы открыть все элементы вышее кнопки + кнопку (чекбокс, радио)
        btn = browser.find_element(By.CLASS_NAME, "btn")
        browser.execute_script("return arguments[0].scrollIntoView(true);", btn)

        # заполняю чекбокс
        robot_checkbox = browser.find_element(By.ID, 'robotCheckbox')
        robot_checkbox.click()

        # заполняю radiobutton
        robot_radiobtn = browser.find_element(By.ID, "robotsRule")
        robot_radiobtn.click()

        btn.click()

        time.sleep(5)


# step_2_2_6()
# =====================================================


# print(os.path.abspath(__file__))  # - выводит полный путь до исполняемого файла
# print(os.path.dirname(__file__))  # - выводит директорию, в которой находится исполняемый файл
# os.path.join(<current_dir>, 'file.txt')  # - для добавления файла (текстового в примере) в указанную директорию


# =====================================================
# открыть страницу
# заполнить форму
# прикрепить файл
# нажать кнопку отправки
def step_2_2_8():
    with webdriver.Chrome(service=Service(ChromeDriverManager().install())) as browser:
        browser.get('http://suninjuly.github.io/file_input.html')

        select_values = {1: 'firstname', 2: 'lastname', 3: 'email'}
        required_values = ['Arseniy', 'Kosolapov', 'hllwwrld@gmail.com']

        required_forms = [
            browser.find_element(By.CSS_SELECTOR, f'.form-group input.form-control[name="{select_values[i]}"]') for i in
            range(1, 4)]
        for i in range(len(required_forms)):
            required_forms[i].send_keys(required_values[i])

        with open('temp.txt', 'w'):
            pass

        curr_dir = os.path.dirname(__file__)
        file_path = os.path.join(curr_dir, 'temp.txt')

        to_upload = browser.find_element(By.CSS_SELECTOR, '#file[accept=".txt"]')
        to_upload.send_keys(file_path)

        btn = browser.find_element(By.CLASS_NAME, "btn")
        btn.click()

        time.sleep(5)

# step_2_2_8()
# =====================================================


# =====================================================
# Открыть страницу http://suninjuly.github.io/alert_accept.html
# Нажать на кнопку
# Принять confirm
# На новой странице решить капчу для роботов, чтобы получить число с ответом
def step_2_3_4():
    with webdriver.Chrome(service=Service(ChromeDriverManager().install())) as browser:
        browser.get('http://suninjuly.github.io/alert_accept.html')

        btn = browser.find_element(By.CSS_SELECTOR, '[type="submit"]')
        btn.click()

        alert_elem = browser.switch_to.alert
        alert_elem.accept()

        x_elem = browser.find_element(By.ID, 'input_value')
        x = int(x_elem.text)

        # нахожу форму для ввода посчитанного значения по x, заполняю форму
        input_form = browser.find_element(By.ID, 'answer')
        input_form.send_keys(calc(x))

        btn = browser.find_element(By.CLASS_NAME, "btn")
        btn.click()

        time.sleep(5)

# step_2_3_4()
# =====================================================


# =====================================================
# Открыть страницу
# Нажать на кнопку
# Переключиться на новую вкладку
# Пройти капчу для робота и получить число-ответ
def step_2_3_6():
    with webdriver.Chrome(service=Service(ChromeDriverManager().install())) as browser:
        browser.get('http://suninjuly.github.io/redirect_accept.html')

        btn = browser.find_element(By.CSS_SELECTOR, '.trollface.btn')
        btn.click()

        new_tab = browser.window_handles[1]

        browser.switch_to.window(new_tab)

        x_elem = browser.find_element(By.ID, 'input_value')
        x = int(x_elem.text)

        # нахожу форму для ввода посчитанного значения по x, заполняю форму
        input_form = browser.find_element(By.ID, 'answer')
        input_form.send_keys(calc(x))

        btn = browser.find_element(By.CLASS_NAME, "btn")
        btn.click()

        time.sleep(5)


# step_2_3_6()
# =====================================================


# =====================================================
# Неявные ожидания implicit waits:
def step_2_4_5():
    with webdriver.Chrome(service=Service(ChromeDriverManager().install())) as browser:
        # появления элемента 5 секунд и в течении этих 5 секунд каждые 500мс проверять наличие элемента
        browser.implicitly_wait(5)

        browser.get("http://suninjuly.github.io/wait1.html")

        button = browser.find_element(By.ID, "verify")
        button.click()

        message = browser.find_element(By.ID, "verify_message")

        assert "successful" in message.text


# step_2_4_5()
# =====================================================
# Явные ожидания explicit waits:

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def step_2_4_7():
    with webdriver.Chrome(service=Service(ChromeDriverManager().install())) as browser:
        browser.get("http://suninjuly.github.io/wait2.html")

        # говорим Selenium проверять в течение 5 секунд, пока кнопка не станет кликабельной
        # WebDriverWait(browser, wait_time) - принимает браузер, с котором происходит взаимодействие и время ожидания
        vrf_btn_сlickable = WebDriverWait(browser, 5).until(  # until принимает правило ожидания, например ожидания кликабельности элемента
            EC.element_to_be_clickable((By.ID, "verify"))  # element_to_be_clickable(locator) возвращает True, когда element становится кликабельным, иначе False
        )
        # в итоге получается конструкция, когда мы находим элемент, устанавливаем то, что ждем от него, потом устанавливаем время ожидания

        vrf_btn_сlickable.click()  # если получили нашу кнопку, по которой можно кликнуть - кликаем
        message = browser.find_element(By.ID, "verify_message")

        assert "successful" in message.text


# step_2_4_7()
# =====================================================


# =====================================================
# Открыть страницу
# Дождаться, когда цена дома уменьшится до $100 (ожидание нужно установить не меньше 12 секунд)
# Нажать на кнопку "Book"
# Решить уже известную нам математическую задачу (используйте ранее написанный код) и отправить решение
def step_2_4_8():
    with webdriver.Chrome(service=Service(ChromeDriverManager().install())) as browser:
        browser.get("http://suninjuly.github.io/explicit_wait2.html")
        browser.implicitly_wait(5)  # устанавливаю время ожидания появления элементов - 5 сек

        # жду, пока цена дома не станет равной 100 через ожидание текста элемента и время ожидания <= 30 сек
        WebDriverWait(browser, 30).until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, '#price'), '$100'))

        # нахожу кнопу для подтвреждения покупки по выбранной цене
        book_btn = browser.find_element(By.CSS_SELECTOR, '#book.btn')
        book_btn.click()

        # заполняю форму (код из прошлых заданий)
        x_elem = browser.find_element(By.ID, 'input_value')
        x = int(x_elem.text)

        # нахожу форму для ввода посчитанного значения по x, заполняю форму
        input_form = browser.find_element(By.ID, 'answer')
        input_form.send_keys(calc(x))

        btn = browser.find_element(By.CSS_SELECTOR, "#solve")
        btn.click()

        # если заданее верно - выводится alert с ответом - вывожу текст этого alerta
        alert = browser.switch_to.alert
        print(alert.text)


# step_2_4_8()
# =====================================================


# =====================================================
# Классы? пока вообще не понятно, как и зачем применять
# 3.1 шаг 1/2/3
class TestAbs(unittest.TestCase):

    def test_1_6_10_1(self):
        with webdriver.Chrome(service=Service(ChromeDriverManager().install())) as browser:
            browser.get('http://suninjuly.github.io/registration1.html')

            select_values = {1: 'first', 2: 'second', 3: 'third'}
            required_values = ['Arseniy', 'Kosolapov', 'hllwwrld@gmail.com']

            required_forms = [browser.find_element(By.CSS_SELECTOR, f'.first_block input.form-control.{select_values[i]}')
                              for i in range(1, 4)]
            for i in range(len(required_forms)):
                required_forms[i].send_keys(required_values[i])

            time.sleep(3)

            button = browser.find_element(By.CSS_SELECTOR, "button.btn")
            button.click()

            time.sleep(1)

            welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
            welcome_text = welcome_text_elt.text

            # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
            self.assertEqual("Congratulations! You have successfully registered!", welcome_text, 'попа')

    def test_1_6_10_2(self):
        with webdriver.Chrome(service=Service(ChromeDriverManager().install())) as browser:
            browser.get('http://suninjuly.github.io/registration2.html')

            select_values = {1: 'first', 2: 'second', 3: 'third'}
            required_values = ['Arseniy', 'Kosolapov', 'hllwwrld@gmail.com']

            required_forms = [browser.find_element(By.CSS_SELECTOR, f'.first_block input.form-control.{select_values[i]}')
                              for i in range(1, 4)]
            for i in range(len(required_forms)):
                required_forms[i].send_keys(required_values[i])

            time.sleep(3)

            button = browser.find_element(By.CSS_SELECTOR, "button.btn")
            button.click()

            time.sleep(1)

            welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
            welcome_text = welcome_text_elt.text

            # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
            self.assertEqual("Congratulations! You have successfully registered!", welcome_text, 'попа')


if __name__ == "__main__":
    unittest.main()
# =====================================================





# =====================================================================================================================
# PYTEST


class TestMainPage1:
    # вызываем фикстуру в тесте, передав ее как параметр
    def test_guest_should_see_login_link(self, browser):
        browser.get('http://selenium1py.pythonanywhere.com/')
        browser.find_element(By.CSS_SELECTOR, "#login_link")

    def test_guest_should_see_basket_link_on_the_main_page(self, browser):
        browser.get('http://selenium1py.pythonanywhere.com/')
        browser.find_element(By.CSS_SELECTOR, ".basket-mini .btn-group > a")


# на этом тесте фикстура, у которой стоит scope=function и autouse=true (browser1) запуститься сама
def test_temp():
    assert 1 == 1


# указана марка для теста, при запуске
@pytest.mark.temp
def test_temp():
    assert 1 == 1


@pytest.mark.temp
@pytest.mark.xfail  # xfail - марка, помечающая тесты, от которых ожидается падение (ожидаемо падают)
def test_temp():
    assert 1 == 1


@pytest.mark.test_fixture
@pytest.mark.xfail(strict=True)  # параметр sctict=True = помечает ожидаемо падающий тест, как failed, если он неожиданно проходит
def test_succeed():
    assert True


@pytest.mark.test_fixture
@pytest.mark.skip  # skip - марка, помечающая тесты, которые должны быть пропущены
def test_skipped():
    assert False


@pytest.mark.test_param_1
# parametrize - марка, позволяющая запустить тест несколько раз с разными параметрами
# первый параметр - название параметра, который будет принимать значения из списка переданного в параметре 2.
# тест запускается с каждым значением из переданного списка
# параметризацию можно так-же задавать и для целого класса
@pytest.mark.parametrize('value_to_compare', [1, 2])
def test_params(value_to_compare):  # указанная в марке parametrize переменная
    assert value_to_compare == 1


class TestParametrize:
    lesson_numbers = ['236895', '236896', '236897', '236898', '236899', '236903', '236904', '236905']

    @pytest.mark.parametrize('lesson_num', lesson_numbers)
    def test_auth_submit_answer(self, browser, lesson_num):
        browser.get(f'https://stepik.org/lesson/{lesson_num}/step/1')

        browser.implicitly_wait(10)

        stepik_auth(browser)

        time.sleep(10)

        assert WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.textarea')))
        answer_input_form = browser.find_element(By.CSS_SELECTOR, '.textarea')

        answer = str(math.log(int(time.time() + 0.2)))
        answer_input_form.send_keys(answer)

        assert WebDriverWait(browser, 1).until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.submit-submission')))
        submit_button = browser.find_element(By.CSS_SELECTOR, '.submit-submission')
        submit_button.click()

        feedback_shown = WebDriverWait(browser, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.smart-hints__hint')))

        if feedback_shown:
            feedback = browser.find_element(By.CSS_SELECTOR, '.smart-hints__hint')
            if feedback.text != 'Correct!':
                print(feedback.text)


def test_open_mozilla(browser_mozilla):
    browser_mozilla.get('https://stepik.org/lesson/237240/step/6?unit=209628')