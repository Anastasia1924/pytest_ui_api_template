import allure
import requests
from pytest_ui_api_template.pages.ApiClass import ApiClass
from pytest_ui_api_template.tests.DataForTests import DataForTests
import json


@allure.epic("API тесты")
@allure.title("Получение полного списка фильмов")
@allure.feature("Позитивные проверки")
@allure.description("В результате проверяется, что статус-код = 200")
@allure.severity("Critical")
def test_get_list():
    api = ApiClass()
    body = api.get_all_films()
    assert body.status_code == 200


@allure.epic("API тесты")
@allure.title("Получение фильма по ID")
@allure.feature("Позитивные проверки")
@allure.description("В результате проверяется, что название = Лорды раздевалки")
@allure.severity("Critical")
def test_get_film_by_id():
    api = ApiClass()
    resp = api.get_film_by_id()
    json_film = resp.json()
    assert "Лорды раздевалки" == json_film['nameRu']


@allure.epic("API тесты")
@allure.title("Получение фильма по названию")
@allure.feature("Позитивные проверки")
@allure.description("В результате проверяется, что статус-код = 200")
@allure.severity("Critical")
def test_get_film_by_name():
    api = ApiClass()
    body = api.get_film_by_name()
    assert body.status_code == 200


@allure.epic("API тесты")
@allure.title("Получение данных о наградах сериала 'Друзья'")
@allure.feature("Позитивные проверки")
@allure.description("В результате проверяется, что статус-код=200 и ответ возвращается не пустой ")
@allure.severity("Critical")
def test_get_data_awards_by_friends():
    api = ApiClass()
    body = api.get_data_awards_by_friends()
    assert body.status_code == 200
    json_resp = body.json
    assert json_resp is not None


@allure.epic("API тесты")
@allure.title("Отправка запроса без ключа")
@allure.feature("Негативная проверка")
@allure.description("В результате проверяется, что статус-код = 401 и выходит сообщение об ошибке")
@allure.severity("Medium")
def test_all_no_apy_key():
    api = ApiClass()
    body = api.get_all_no_apy_key()
    assert body.status_code == 401
    json_resp = body.json()
    assert "You don't have permissions. See https://kinopoiskapiunofficial.tech" == json_resp['message']
