### skypro_final_diplom
## Дипломная работа.

### Стек

    pytest
    selenium
    request
    allure

### Библиотеки

    pip install pytest
    pip install selenium
    pip install webdriver-manager
    pip install allure

### Шаги
1. Склонировать проект 'git clone https://github.com/SergeyQA51/pytest_ui_api_template.git
   pytest_ui_api_template.git'
2. Установить зависимости
3. Запустить тесты:
    UI - 'pytest tests/test_ui.py -s -v'
    API - 'pytest tests/test_api.py -s -v'
    UI+API - 'pytest -n auto'
5. Открыть отчет 'allure open allure-report'

### Структура проекта
- ./tests - тесты
- ./page - описание страниц
- config.json - ссылки на ресурсы, токен авторизации

### Полезные ссылки
- [Генератор файла .gitignore] (https://www.toptal.com/developers/gitignore?ysclid=m0jp8h70zl115674830)
- Ссылка на финальный проект : 

### Библиотеки
- pip install pytest
- pip install selenium
- pip install webdriver-manager
- pip install allure-pytest
- pip install pytest-xdist

### Создание файла JSON для доступа к проекту тестирования

1. Создайте в проекте файл с названием config.json

2. Введите следующую структуру JSON:
{  
    "url": "https://www.chitai-gorod.ru",  
    "cookie_policy": {  
        "name": "cookie_policy",  
        "value": "1"  
    },  
    "base_url": "https://web-gate.chitai-gorod.ru/api/v1",  
    "base_url_v2": "https://web-gate.chitai-gorod.ru/api/v2",  
    "token": "Вставить сюда значение "access-token" из панели разработчика вашего браузера [Читай-город](https://www.chitai-gorod.ru)"  
}  
