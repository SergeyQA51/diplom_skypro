import allure
import pytest
from selenium import webdriver
from page.MainPage import MainPage



@allure.title("Открытие сайта")
@allure.description("Проверка загрузки главной страницы")
@allure.feature("READ")
@allure.severity("blocker")
@pytest.mark.positive_test
def test_chitai_gorod(): 
    with allure.step("Открытие веб-страницы в Chrome и выполнение поиска"):
        browser = webdriver.Chrome() 
        main_page = MainPage(browser) 
        main_page.set_cookie_policy()


@allure.title("Поиск книги на кириллице")
@allure.description("Проверка получения книг на кириллице")
@allure.feature("READ")
@allure.severity("blocker")
@pytest.mark.ui_test
@pytest.mark.positive_test
def test_search_book_rus_ui():
    with allure.step("Открытие веб-страницы в Chrome, поиск книги на кириллице"):
        browser = webdriver.Chrome()
        main_page = MainPage(browser) 
        main_page.set_cookie_policy()
        text = main_page.search_book_rus_ui('горе от ума')
        assert text [0:46] == 'Показываем результаты по запросу «горе от ума»'


@allure.title("Поиск книги на латинице")
@allure.description("Проверка получения книг на латинице")
@allure.feature("READ")
@allure.severity("blocker")
@pytest.mark.ui_test
@pytest.mark.positive_test
def test_search_book_eng_ui():
    with allure.step("Открытие веб-страницы в Chrome, поиск книги на латинице"):
        browser = webdriver.Chrome()
        main_page = MainPage(browser) 
        main_page.set_cookie_policy()
        text = main_page.search_book_eng_ui('avengers')
        assert text [0:43] == "Показываем результаты по запросу «avengers»"


@allure.title("Поиск по символам юникода")
@allure.description("Проверка поиска по символам")
@allure.feature("READ")
@allure.severity("blocker")
@pytest.mark.ui_test
@pytest.mark.negative_test
def test_search_invalid_ui():
    with allure.step("Открытие веб-страницы в Chrome, ввод символов"):
        browser = webdriver.Chrome()
        main_page = MainPage(browser) 
        main_page.set_cookie_policy()
        text = main_page.search_invalid_ui('))))))))))')
        assert text [0:24] == "Похоже, у нас такого нет"


@allure.title("Поиск по каталогу")
@allure.description("Тест проверяет корректное выполнение поиска, используя каталог")
@allure.feature("READ")
@allure.severity("normal")
@pytest.mark.positive_test
def test_catalog_search():
    with allure.step("Открытие веб-страницы в Chrome и выполнение поиска"):
        browser = webdriver.Chrome()
        main_page = MainPage(browser) 
        main_page.set_cookie_policy()
        text = main_page.catalog_search() 
    with allure.step("Проверка текста в выбранной категории каталога"):
        assert text[0:14] == "ПОЭЗИЯ И СТИХИ"


@allure.title("Проверка пустой корзины")
@allure.description("Проверка, что в пустой корзине появляется сообщение 'В корзине ничего нет'")
@allure.feature("")
@allure.severity("blocker")
@pytest.mark.positive_test
def test_get_empty_result_message():
    with allure.step("Открытие веб-страницы в Chrome"):
        browser = webdriver.Chrome()
        main_page = MainPage(browser)
        main_page.set_cookie_policy() 
    with allure.step("Проверка пустой корзины с сообщением 'В корзине ничего нет'"):  
        msg = main_page.get_empty_result_message()  
    print(f"Полученное сообщение: {msg}")  # Дополнительное логирование для отладки  
    assert msg == "В корзине ничего нет"   

       
@allure.title("Проверка пустой корзины")
@allure.description("Проверка, что в пустой корзине появляется сообщение 'В корзине ничего нет'")
@allure.feature("")
@allure.severity("blocker")
@pytest.mark.positive_test
def test_get_empty_result_message():
    with allure.step("Открытие веб-страницы в Chrome"):
        browser = webdriver.Chrome()
        main_page = MainPage(browser)
        main_page.set_cookie_policy() 
    with allure.step("Проверка пустой корзины с сообщением 'В корзине ничего нет'"):
        msg = main_page.get_empty_result_message()
        assert msg == "В корзине ничего нет"
    with allure.step("Зактытие браузера"):
        main_page.close_driver()