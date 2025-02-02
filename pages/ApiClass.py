import requests
from pytest_ui_api_template.tests.DataForTests import DataForTests
import json
import allure
from requests.models import Response

class ApiClass:
    def __init__(self):
        self.headers = {
            "Authorization": DataForTests.x_api_key,
            }

    @allure.step("Получение полного списка фильмов")
    def get_all_films(self):
        data = DataForTests()
        url = data.base_url_api + "films"
        resp = requests.get(url, headers=self.headers)
        body = resp.json()  # Исправлено на вызов метода .json()
        return body

    @allure.step("Поиск фильма по ID")
    def get_film_by_id(self):
        data = DataForTests()
        url = data.base_url_api + "films" + data.kinopoisk_id
        resp = requests.get(url, headers=self.headers)
        return resp