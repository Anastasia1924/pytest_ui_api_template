import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webelement import WebElement
from selenium.common.exceptions import TimeoutException

@allure.epic("UI тесты")
class MainPage:

    def __init__(self, driver):
        self._driver = driver
        self._driver.maximize_window()
        self.wait = WebDriverWait(driver, 10)

    @allure.step("Открытие формы(переход на страницу)")
    def open_form(self):
        self._driver.get("https://www.kinopoisk.ru")

    @allure.step("Ввод фразы в поиск")
    def enter_search_name(self, name: str):
        search_input = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "input[name=kp_query]")))
        search_input.clear()
        search_input.send_keys(name)

    @allure.step("Клик на 'лупу' в строке поиска")
    def submit_search(self):
        search_button = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[tipe=submit]")))
        search_button.click()

    @allure.step("Получение списка фильмов по предварительному поиску")
    def get_search_preview_results(self):
        self.wait.until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, "h4.kinopoisk-header-suggest-item__title a")))
        film_links_titles = self._driver.find_elements(By.CSS_SELECTOR, "h4.kinopoisk-header-suggest-item__title a")
        return [film_title.text for film_title in film_links_titles]

    @allure.step("Поиск случайного фильма по жанру")
    def search_by_genre_random(self, genre: str):
        self._driver.find_element(By.ID, "genreListTitle").click()
        self._driver.find_element(
            By.CSS_SELECTOR, f"input[data-name='{genre}']").is_selected()
        self._driver.find_element(By.ID, "genreListTitle").click()
        self._driver.find_element(By.ID, "search").click()

    @allure.step("Получение названия произвольного фильма")
    def get_film_title(self):
        film_title_element = self.wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "div.filmName a"))
        )
        return film_title_element.text if film_title_element else None


    @allure.step("Оценить фильм")
    def evaluate_the_film(self):
        self._driver.find_element(By.CSS_SELECTOR, "a[data-tid='73187f6b']").click()
        self._driver.find_element(By.CSS_SELECTOR, "button=Оценить фильм").click()
        self._driver.find_element(By.CSS_SELECTOR, "button[aria-label='Оценка 10']").click()












