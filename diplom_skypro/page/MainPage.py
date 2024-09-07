import json  
import allure   
from selenium.webdriver.common.by import By  
from selenium.webdriver.support.ui import WebDriverWait  
from selenium.webdriver.support import expected_conditions as EC    

# Загрузка настроек из файла config.json  
with open('config.json') as config_file:  
    config = json.load(config_file)  

class MainPage:  
    def __init__(self, driver):  
        self._driver = driver  
        self._driver.maximize_window()  
        self.load_config()  
        self._driver.get(self.config["url"])  
        self._driver.implicitly_wait(8)    
    
    def load_config(self):   
        with open('config.json') as config_file:  
            self.config = json.load(config_file)   

    @allure.step("Политика куки")  
    def set_cookie_policy(self):   
        cookie = config["cookie_policy"]  
        self._driver.add_cookie(cookie)  

    @allure.step("Поиск книги на кириллице")  
    def search_book_rus_ui(self, term):  
        self._driver.find_element(By.CLASS_NAME, "header-search__input").send_keys(term)  
        self._driver.find_element(By.CLASS_NAME, "header-search__button").click()  
        txt = self._driver.find_element(By.XPATH, '//*[@id="__layout"]/div/div[3]/div[1]/p').text  
        return txt  

    @allure.step("Поиск книги на латинице")  
    def search_book_eng_ui(self, term):  
        self._driver.find_element(By.CLASS_NAME, "header-search__input").send_keys(term)  
        self._driver.find_element(By.CLASS_NAME, "header-search__button").click()  
        txt = self._driver.find_element(By.XPATH, '//*[@id="__layout"]/div/div[3]/div[1]/p').text  
        return txt  

    @allure.step("Ввод невалидного значения")    
    def search_invalid_ui(self, term):  
        self._driver.find_element(By.CLASS_NAME, "header-search__input").send_keys(term)  
        self._driver.find_element(By.CLASS_NAME, "header-search__button").click()  
        txt = self._driver.find_element(By.CLASS_NAME, "catalog-empty-result__description").text  
        return txt  

    @allure.step("Поиск через каталог")  
    def catalog_search(self):  
        self._driver.find_element(By.XPATH, '//div[contains(text(),"Да, я здесь")]').click()  
        self._driver.find_element(By.XPATH, '//span[contains(text(),"Каталог")]').click()  
        self._driver.find_element(By.XPATH, '//span[contains(text(),"Художественная литература")]').click()  
        self._driver.find_element(By.XPATH, '//span[contains(text(),"Поэзия")]').click()  
        txt = WebDriverWait(self._driver, 5).until(
           EC.presence_of_element_located((By.CLASS_NAME, 'app-catalog-page__title'))
       ).text
        return txt   

    @allure.step("Проверка пустой корзины")  
    def get_empty_result_message(self):  
    # Переход на страницу корзины  
        self._driver.get(config["url"] + "/cart")  
    
        try:  
        # Явное ожидание, чтобы убедиться, что элемент есть на странице  
            empty_message_element = WebDriverWait(self._driver, 10).until(  
                EC.presence_of_element_located((By.CLASS_NAME, "empty-title"))   
        )  
        # Получаем текст сообщения  
            return empty_message_element.text.strip()  
        
        except Exception as e:  
            print(f"Ошибка при получении сообщения о пустой корзине: {e}")  
        return ""  

    @allure.step("Закрытие веб-браузера")  
    def close_driver(self):  
        self._driver.quit()
