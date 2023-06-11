from flask import Flask, render_template, abort, url_for
from datetime import datetime
import random
from model.country import db, find_by_name, find_by_index, find_continent_by_cc, continent_map
from model.squares import Square

app = Flask(__name__)


# 9 kwadracikow, randomowe kolory, mozna klikac, stystyki

@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


@app.route('/date')
def current_date():
    return f'Response time: {str(datetime.now())}'


counter = 0


@app.route('/count')
def count():
    global counter
    counter += 1
    return f'Visit counter: {str(counter)}'


@app.route('/color')
def color():
    mylist = ["red", "blue", "green"]
    return f'{random.choice(mylist)}'


@app.route('/hello-world')
def hello_world_html():
    return render_template('welcome.html', message='Aplikacje Server side są super!')


@app.route('/countries')
def random_country():
    # country_index = random.randint(0,246)
    # country = db[country_index]
    country = random.choice(db)
    return render_template('country.html', country=country)


# Path variable: <typ:nazwa>
# abort służy do wyświetlania błędów
@app.route('/countries/<name>')
def country_by_name(name: str):
    try:
        found_country = find_by_name(name)
    except ValueError as ex:
        abort(404, ex)

    return render_template('country.html', country=found_country)


# Pomimo, że nie moża mieć 2 endpointów o tej samej nazwie, jest to dopiszczalne jeśli tym danych templacie jest inny
# tak jak w @app.route('/countries/<name>') vs @app.route('/countries/<int:index>')
# w tym przypadku to działa, nbo dla flaska są dwa różne endpointy
@app.route('/countries/<int:index>')
def country_by_index(index: int):
    try:
        found_country = find_by_index(index)
        found_country['continent'] = find_continent_by_cc(found_country['cc'])
    except IndexError:
        abort(404, f"Country with index {index} not found!")

    return render_template('country_index.html', country=found_country, index=index, continent_map=continent_map)


squares_list = []


def create_squares():
    global squares_list
    squares_list = []
    for i in range(9):
        squares_list.append(Square())


@app.route('/squares')
def squares():
    create_squares()
    return render_template('squares.html', squares_list=squares_list)


@app.route('/squares/<int:index>')
def increment_counter_squares(index: int):
    found_square = squares_list[index]
    found_square.counter = found_square.counter + 1

    return render_template('squares.html', squares_list=squares_list)


# Lista endpointów zdefiniowanych dla applikacji
print(app.url_map)

if __name__ == '__main__':
    app.run()
