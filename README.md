# Дипломная работа по автоматизации тестирования на основании курсовой работы по ручному тестированию сайта "Кинопоиск"
### Ссылка на курсовую по ручному тестированию сайта "Кинопоиск"
- [https://mystude.yonote.ru/share/77fcc389-2b1e-4f04-adc1-74305a89e599]
### Для тестирования использовались UA и Api тесты 
#### Сайт "Кинопоиск"
- [https://www.kinopoisk.ru]
#### Документация API
- [https://api.kinopoisk.dev/v1.4]

## Используемые библиотеки
- allure
- pytest
- requests
- selenium
- webdriver-manager
## Структура проекта
- pages/
  - ApiClass.py
  - MainPage.py
- tests/
  - DataForTests.py
  - test_api.py
  - test_ui.py
- README.md
- requirements.txt
- pytest.ini
- .gitignore
## Инструкция по работе с проектом
- Запуск тестов UI по команде: `pytest -v --alluredir=allure-results tests\test_ui.py`
- Генерация отчета по команде: `allure serve allure-results`