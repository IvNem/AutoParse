import json
import locale
import os

from staticjinja import Site


# Создаем список json файлов
def collect_data_filepaths(directory_path='data', ):
    for file in os.listdir(directory_path):
        if file.endswith(".json"):
            yield os.path.join(directory_path, file)


if __name__ == "__main__":
    locale.setlocale(locale.LC_ALL, '')

    # Получаем список json файлов
    data_filepaths = list(collect_data_filepaths())

    cars = []
    # Компонуем общий список из нескольких файлов
    for filename in data_filepaths:
        with open(filename, 'r') as file:
            site_cars = json.loads(file.read())
            cars.extend(site_cars)

    site = Site.make_site(env_globals={
        'cars': cars,
    })

    site.render(use_reloader=True)
