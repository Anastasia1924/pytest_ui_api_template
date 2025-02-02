import allure
import requests
from pytest_ui_api_template.pages.ApiClass import ApiClass
from pytest_ui_api_template.tests.DataForTests import DataForTests
import json


@allure.epic("API тесты")
@allure.title("Получение полного списка фильмов")
@allure.feature("Позитивные проверки")
@allure.description("В результате проверяется, что список больше 0")
@allure.severity("Critical")
def test_get_list():
    api = ApiClass()
    body = api.get_all_films()
    assert len(body) > 0


@allure.epic("API тесты")
@allure.title("Получение фильма по ID")
@allure.feature("Позитивные проверки")
@allure.description("В результате проверяется...")
@allure.severity("Critical")
def test_get_film_by_id():
    api = ApiClass()
    api.get_film_by_id()

    # проверки не знаю как сделать


@allure.epic("API тесты")
@allure.title("Получение фильма по ID")
@allure.feature("Позитивные проверки")
@allure.description("В результате проверяется...")
@allure.severity("Critical")
def test_get_film_by_name():
    api = ApiClass()
    api.get_film_by_name()

    # проверки не знаю как сделать

@allure.epic("API тесты")
@allure.title("Получение данных о наградах сериала 'Друзья'")
@allure.feature("Позитивные проверки")
@allure.description("В результате проверяется...")
@allure.severity("Critical")
def test_get_data_awards_by_friends():
    api = ApiClass()
    body = api.get_data_awards_by_friends()
    assert len(body) > 0

