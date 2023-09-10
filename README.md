# Асинхронный парсер PEP

Парсер, собирающий информацию с сайта https://www.python.org/
- версии языка и авторов версий;
- статусы всех стандартов PEP.

Вся собранная информация сохраняется в файлы с расширением **csv**:
- Информация о стандарте: номер, статус, автор-(ы);
- Колличество каждого статуса на сайте + общая сумма.

## Используемые технологии

- [Python](https://www.python.org/) 3.7.9
- [Scrapy](https://scrapy.org/) 2.5.1

## Запуск парсера

1. Скопируйте проект с помощью следующей команды:

    ```bash
    git clone https://github.com/Duckin1/scrapy_parser_pep.git
    ```

2. Установите и активируйте виртуальное окружение:

    ```bash
    python3 -m venv venv
    source venv/Scripts/activate  # Для Windows
    source venv/bin/activate  # Для Linux/Mac
    ```

3. Установите зависимости:

    ```bash
    pip install -r requirements.txt
    ```

4. Запустите парсер из директории `scrapy_parser_pep`:

    ```bash
    scrapy crawl pep
    ```

## Результаты

В папке results появятся 2 файла формата .csv в которых будет результаты работы парсера 

## Автор

- [Алмаз Миннибаев](https://github.com/Duckin1)