from mytoken import YA_TOKEN
from main import get_folder, create_folder, headers
import pytest

wrong_token = 'qklqwejeogneginqogjn'
wrong_headers = {
    f'Authorization': 'OAuth {}'.format(wrong_token)
}

# Создаю параметры для теста. Название папки, заголовки, возвращаемый код
params = [
    ('aFolder N1', headers, 201), #папка создана
    ('aFolder N1', headers, 409), #папка уже существует
    ('aFolder NN', wrong_headers, 401), #неавторизованный пользователь
    ('anewFolder', headers, 201),    #папка создана
    ('aFOLder1', headers, 201) #папка создана
]

# Создаю параметры для второго теста. Название папки, возвращаемый код
params2 = [
    ('aFolder N1', headers), #папка есть на диске
    ('anewFolder', headers), #папка есть на диске
    ('aFOLder1', headers)    #папка есть на диске
]

@pytest.mark.parametrize('foldername, headers, result', params)
def test_create_folder(foldername, headers, result):
    # Тест проверяет функцию создания папки путем проверки кода ответа
    assert create_folder(headers=headers, foldername=foldername) == result

@pytest.mark.parametrize('foldername, headers', params2)
def test_create_folder_2(foldername, headers):
    # Тест проверяет наличие папок созданных тестом N1 через функцию получения папки. Если 200 - папка существует
    assert get_folder(headers=headers, foldername=foldername) == 200
