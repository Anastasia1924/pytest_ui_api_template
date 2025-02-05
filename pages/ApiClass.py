import requests
from pytest_ui_api_template.tests.DataForTests import DataForTests
import json
import allure
from requests.models import Response

class ApiClass:
    def __init__(self):
        self.headers = {
            "x-api-key": DataForTests.x_api_key,
            }
        self.headers_dev = {
            "x-api-key": DataForTests.x_api_key_dev,
        }

    @allure.step("Получение полного списка фильмов")
    def get_all_films(self):
        data = DataForTests()
        url = data.base_url_api + "films"
        resp = requests.get(url, headers=self.headers)
        return resp

    @allure.step("Поиск фильма по ID")
    def get_film_by_id(self):
        data = DataForTests()
        url = data.base_url_api + "films/" + data.kinopoisk_id
        resp = requests.get(url, headers=self.headers)
        return resp

    @allure.step("Поиск фильма по названию")
    def get_film_by_name(self):
        data = DataForTests()
        url = data.base_url_api_dev + "films/" + data.name_ru
        resp = requests.get(url, headers=self.headers_dev)
        return resp

    @allure.step("Получение данных о наградах сериала 'Друзья'")
    def get_data_awards_by_friends(self):
        data = DataForTests()
        url = data.base_url_api + "films/" + data.friend_id + "/awards"
        resp = requests.get(url, headers=self.headers)
        return resp


    @allure.step("Получение списка без api_key")
    def get_all_no_apy_key(self):
        data = DataForTests()
        url = data.base_url_api + "films"
        resp = requests.get(url)
        return resp
