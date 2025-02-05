import allure
import pytest
from pytest_ui_api_template.pages.MainPage import MainPage
from pytest_ui_api_template.config import *


@allure.epic("UI тесты")
@allure.title("Название заголовка")
@allure.feature("Позитивные проверки")
@allure.description("В результате проверяется название заголовка")
@allure.severity("Critical")
def test_browser_title(browser):
    with allure.step("Переход на главную страницу)"):
        main_page = MainPage(browser)
        main_page.open_page(base_url)
        browser_title = browser.title
        assert browser_title == "Кинопоиск. Онлайн кинотеатр. Фильмы сериалы мультфильмы и энциклопедия"


@allure.epic("UI тесты")
@allure.title("Поиск фильмов по названию")
@allure.feature("Позитивные проверки")
@allure.description("В результате проверяется , что введённое значение есть в названии первого фильма")
@allure.severity("Critical")
@pytest.mark.parametrize("film_title", ["Король Лев", "Титаник", "Зеленая миля"])
@pytest.mark.positive
@pytest.mark.smoke
def test_fast_search_by_film_title(browser, film_title):
    with allure.step("Переход на главную страницу)"):
        main_page = MainPage(browser)
        main_page.open_page(base_url)

    with allure.step("Ввод названия фильма в поисковую строку"):
        main_page.enter_search_name(film_title)

    with allure.step("Получить название фильмы"):
        list_elements = main_page.get_search_preview_results()

    with allure.step("Проверить, что введённое значение есть в названии первого фильма"):
        assert film_title in list_elements, f"Ожидалось, что фильм {film_title} будет в результатах поиска"


@allure.epic("UI тесты")
@allure.title("Поиск фильмов по жанру")
@allure.feature("Позитивные проверки")
@allure.description("В результате проверяется")
@allure.severity("Critical")
@pytest.mark.parametrize("film_genre", ["комедия", "аниме", "музыка"])
@pytest.mark.positive
@pytest.mark.smoke
def test_search_for_genre(browser, film_genre):
    with allure.step("Переход на главную страницу)"):
        main_page = MainPage(browser)
        main_page.open_page(base_url)

    with allure.step("В поисковой строке нажатие на 'поиск'"):
        main_page.submit_search()

    with allure.step("В поисковой строке нажатие на 'поиск'"):
        main_page.search_by_genre_random(film_genre)
        film_title = main_page.get_film_title()
        assert film_title, "Название фильма пустое!"


# Оценить фильм:
@allure.epic("UI тесты")
@allure.title("Оценка фильма")
@allure.feature("Позитивные проверки")
@allure.description("В результате проверяется")
@allure.severity("Critical")
@pytest.mark.parametrize("film_title, film_id, rating", [("Фантомас", 522876, 10)])
@pytest.mark.positive
def test_rate_film(browser, film_title, film_id, rating):
    with allure.step("Переход на главную страницу)"):
        main_page = MainPage(browser)
        main_page.open_page(base_url)

# 1. Ввести название фильма "Фантомас"
    with allure.step("Ввод названия фильма в поисковую строку"):
        main_page.enter_search_name(film_title)

# 2. Провалиться в найденный фильм.
    with allure.step("Клик по первому названию"):
        main_page.select_film(film_id)

# 3. Нажать кнопку оценить фильм.
    with allure.step("Нажать на 'Оценить фильм'"):
        main_page.click_rate_film()

# 4. Выбрать 10
    with allure.step("Оценить фильм"):
        main_page.rate_film(rating)

# 5. Проверить, что оценка 10
    with allure.step("Проверка рейтинга"):
        rating = main_page.get_rating()
        assert rating == 10, f"Ожидалось, что рейтинг будет 10, но получено: {rating}"


# Добавить фильм в "буду смотреть".
@allure.epic("UI тесты")
@allure.title("Добавить фильм в ' Буду смотреть'")
@allure.feature("Позитивные проверки")
@allure.description("В результате проверяется")
@allure.severity("Critical")
@pytest.mark.parametrize("film_title", ["125jkhyf"])
@pytest.mark.positive
def test_empty_search(browser, film_title):
    with allure.step("Переход на главную страницу)"):
        main_page = MainPage(browser)
        main_page.open_page(base_url)

# Ввести произвольный набор символов
    with allure.step("Ввод названия фильма в поисковую строку"):
        main_page.enter_search_name(film_title)

# Подтвердить поиск"
    with allure.step("Подтверждение поиска"):
        main_page.submit_search()

# Получение сообщения "К сожалению по вашему запросу ничего не найдено"
    with allure.step("Подтверждение поиска"):
        empty_message = main_page.get_empty_message()
        assert empty_message == "К сожалению, по вашему запросу ничего не найдено..."
