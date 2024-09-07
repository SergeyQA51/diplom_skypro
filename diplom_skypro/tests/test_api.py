import requests  
import allure  
import pytest  
import json  

  
with open('config.json') as config_file:  
    config = json.load(config_file)  

BASE_URL = config["base_url"]  
BASE_URL_2 = config["base_url_v2"]  
TOKEN = config["token"]  

@allure.feature("API")  
@allure.story("Получение списка книг")  
@pytest.mark.api_test  
@pytest.mark.positive_test  
def test_get_books():  
    headers = {  
        'content-type': 'application/json',  
        'authorization': f'Bearer {TOKEN}'  
    }  
    response = requests.get(f"{BASE_URL_2}/products", headers=headers)  
    assert response.status_code == 200, f"Ожидался статус-код 200, но получен {response.status_code}"  

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
    headers = {  
        'content-type': 'application/json',  
        'authorization': f'Bearer {TOKEN}'  
    }  
    response = requests.get(f"{BASE_URL_2}/search/product?phrase=горе от ума", headers=headers)  
    assert response.status_code == 200, f"Ожидался статус-код 200, но получен {response.status_code}"  

@allure.feature("API")  
@allure.story("Поиск книг на латинице")  
@pytest.mark.api_test  
@pytest.mark.positive_test  
def test_search_books_eng():  
    headers = {  
        'content-type': 'application/json',  
        'authorization': f'Bearer {TOKEN}'  
    }  
    response = requests.get(f"{BASE_URL_2}/search/product?phrase=avengers", headers=headers)  
    assert response.status_code == 200, f"Ожидался статус-код 200, но получен {response.status_code}"  

@allure.feature("API")  
@allure.story("Пустое поле поиска")  
@pytest.mark.api_test  
@pytest.mark.negative_test  
def test_search_empty():  
    headers = {  
        'content-type': 'application/json',  
        'authorization': f'Bearer {TOKEN}'  
    }  
    response = requests.get(f"{BASE_URL_2}/search/product?phrase=", headers=headers)  
    assert response.status_code == 400, f"Ожидался статус-код 400, но получен {response.status_code}"  
    assert 'Phrase обязательное поле' in response.text  

@allure.feature("API")  
@allure.story("Пробел")  
@pytest.mark.api_test  
@pytest.mark.negative_test  
def test_search_space():  
    headers = {  
        'content-type': 'application/json',  
        'authorization': f'Bearer {TOKEN}'  
    }  
    response = requests.get(f"{BASE_URL_2}/search/product?phrase=   ", headers=headers)  
    assert response.status_code == 422, f"Ожидался статус-код 422, но получен {response.status_code}"  

@allure.feature("API")  
@allure.story("Получение списка книг по автору")  
@pytest.mark.api_test  
@pytest.mark.positive_test  
def test_get_books_by_author():      
    headers = {  
        'content-type': 'application/json',  
        'authorization': f'Bearer {TOKEN}'  
    }  
    response = requests.get(f"{BASE_URL_2}/products/facet?filters[authors]=593251", headers=headers)  
    assert response.status_code == 200, f"Ожидался статус-код 200, но получен {response.status_code}"
