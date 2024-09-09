import requests  
import allure  
import pytest  
import json  

# Загрузка конфигурации
with open('config.json') as config_file:  
    config = json.load(config_file)  

BASE_URL = config["base_url"]  
BASE_URL_2 = config["base_url_v2"]  
TOKEN = config["token"]  

def get_headers():
    """Возвращает заголовки для запросов."""
    return {  
        'Content-Type': 'application/json',  
        'Authorization': f'Bearer {TOKEN}'  
    }  

def make_request(method, endpoint, **kwargs):
    """Функция для выполнения HTTP-запросов."""
    url = f"{BASE_URL_2}{endpoint}"  
    response = requests.request(method, url, headers=get_headers(), **kwargs)
    return response

@allure.feature("API")  
@allure.story("Получение списка книг")  
@pytest.mark.api_test  
@pytest.mark.positive_test  
def test_get_books():  
    response = make_request("GET", "/products")  
    assert response.status_code == 200, f"Ожидался статус-код 200, но получен {response.status_code}"

@allure.feature("API")
@allure.story("Получение книги по ID")
@pytest.mark.api_test
@pytest.mark.positive_test
def test_get_book_by_id():
    book_id = "gore-ot-uma-2499954"
    url = f"{BASE_URL}/products/slug/{book_id}"
    print(f"Запрос к URL: {url}")  # Отладочное сообщение
    response = make_request("GET", url)
    assert response.status_code == 200, f"Ожидался статус-код 200, но получен {response.status_code}"

    # Проверка наличия ключевых слов в теле ответа
    assert "Александр" in response.text and "Грибоедов" in response.text, "Ожидаемые автор и название книги не найдены в ответе"   

@allure.feature("API")  
@allure.story("Получение информации о книге по ID")  
@pytest.mark.api_test  
@pytest.mark.positive_test  
def test_get_book_by_id():  
    book_id = "gore-ot-uma-2499954"    
    headers = {  
        'content-type': 'application/json',  
        'authorization': f'Bearer {TOKEN}'  
    }  

    response = requests.get(f"{BASE_URL}/products/slug/{book_id}", headers=headers)  
    assert response.status_code == 200, f"Ожидался статус-код 200, но получен {response.status_code}"  
    assert "Александр" in response.text and "Грибоедов" in response.text

@allure.feature("API")  
@allure.story("Поиск книг на кириллице")  
@pytest.mark.api_test  
@pytest.mark.positive_test  
def test_search_books_rus():  
    response = make_request("GET", f"/search/product?phrase=горе от ума")  
    assert response.status_code == 200, f"Ожидался статус-код 200, но получен {response.status_code}"  

@allure.feature("API")  
@allure.story("Поиск книг на латинице")  
@pytest.mark.api_test  
@pytest.mark.positive_test  
def test_search_books_eng():  
    response = make_request("GET", f"/search/product?phrase=avengers")  
    assert response.status_code == 200, f"Ожидался статус-код 200, но получен {response.status_code}"  

@allure.feature("API")  
@allure.story("Пустое поле поиска")  
@pytest.mark.api_test  
@pytest.mark.negative_test  
def test_search_empty():  
    response = make_request("GET", f"/search/product?phrase=")  
    assert response.status_code == 400, f"Ожидался статус-код 400, но получен {response.status_code}"  
    assert 'Phrase обязательное поле' in response.text  

@allure.feature("API")  
@allure.story("Пробел")  
@pytest.mark.api_test  
@pytest.mark.negative_test  
def test_search_space():  
    response = make_request("GET", f"/search/product?phrase=   ")  
    assert response.status_code == 422, f"Ожидался статус-код 422, но получен {response.status_code}"  

@allure.feature("API")  
@allure.story("Получение списка книг по автору")  
@pytest.mark.api_test  
@pytest.mark.positive_test  
def test_get_books_by_author():  
    response = make_request("GET", f"/products/facet?filters[authors]=593251")  
    assert response.status_code == 200, f"Ожидался статус-код 200, но получен {response.status_code}"


