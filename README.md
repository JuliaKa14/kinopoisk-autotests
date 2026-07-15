# Автоматизация тестирования Кинопоиска

## Описание проекта
Дипломный проект по автоматизации тестирования сервиса **Кинопоиск**.

Проект включает:

- UI-тесты (Selenium + Pytest)
- API-тесты (Requests + Pytest)
- формирование Allure-отчетов
- использование Page Object
- хранение конфигурации и API-ключей в переменных окружения

## Используемые технологии
- Python 3
- Pytest
- Selenium
- Requests
- Allure Report
- webdriver-manager
- python-dotenv

## Структура проекта
```
api/
pages/
tests/
utils/

config.py
conftest.py
requirements.txt
pytest.ini
README.md
```

## Установка проекта
Клонировать репозиторий

```bash
git clone <ссылка-на-репозиторий>
```

Перейти в папку проекта

```bash
cd kinopoisk-autotests
```

Создать виртуальное окружение

```bash
python -m venv venv
```

Активировать окружение Windows

```bash
venv\Scripts\activate
```

Установить зависимости

```bash
pip install -r requirements.txt
```

## Настройка
Создать файл `.env`

Пример:

```text
API_TOKEN=ваш_api_ключ
BASE_URL=https://api.kinopoisk.dev
```

## Запуск всех тестов

```bash
pytest
```

## Запуск только UI-тестов

```bash
pytest -m "ui"
```

## Запуск только API-тестов

```bash
pytest -m "api"
```

## Формирование Allure-отчета

Запуск тестов

```bash
pytest --alluredir=allure-results
```

Просмотр отчета

```bash
allure serve allure-results
```

## Особенности проекта

- Page Object Model
- отдельный слой API
- использование фикстур Pytest
- Allure Steps
- Allure Title
- аннотации типов
- конфигурация через `.env`
- разделение UI и API тестов маркерами

## Проект по ручному тестированию

Ссылка: https://bagliore.yonote.ru/share/ef4159d4-5aa1-4ac2-baeb-9aa71a19b6db


## Автор
Кузнецова Юлия Романовна, группа 126.2
Дипломный проект по автоматизации тестирования.