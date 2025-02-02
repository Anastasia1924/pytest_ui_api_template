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
        body = resp.json()  #вызов метода .json()
        return body

    @allure.step("Поиск фильма по ID")
    def get_film_by_id(self):
        data = DataForTests()
        url = data.base_url_api + "films" + data.kinopoisk_id
        resp = requests.get(url, headers=self.headers)
        body = resp.json()  # вызов метода .json()
        return body

    @allure.step("Поиск фильма по названию")
    def get_film_by_name(self):
        data = DataForTests()
        url = data.base_url_api + "films" + data.name_ru
        resp = requests.get(url, headers=self.headers)
        return resp

    @allure.step("Получение данных о наградах сериала 'Друзья'")
    def get_data_awards_by_friends(self):
        data = DataForTests()
        url = data.base_url_api + "films" + data.friend_id + "awards"
        resp = requests.get(url, headers=self.headers)
        body = resp.json()  # вызов метода .json()
        return body

