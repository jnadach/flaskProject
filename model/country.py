import json
import pycountry_convert


def __load_db():
    with open('country_info.json', encoding='utf-8') as mock_database:
        return json.load(mock_database)


def find_by_name(name: str):
    for country_data in db:
        if country_data['country'].casefold() == name.casefold():
            return country_data
    raise ValueError(f"Country {name} not found!")


def find_by_index(index: int):
    return db[index]


def find_continent_by_cc(country_code):
    try:
        continent_code = pycountry_convert.country_alpha2_to_continent_code(country_code)
        continent_name = pycountry_convert.convert_continent_code_to_continent_name(continent_code)
        counter = continent_map.get(continent_name, 0)
        continent_map[continent_name] = counter + 1
        return continent_name
    except KeyError:
        return None



continent_map = {}
# Przypisujemy do zmiennej zeby przy imporcie metoda __load_db() była wykonywana tylko raz !!!
db = __load_db()
