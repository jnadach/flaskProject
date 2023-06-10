from flask import Flask
from datetime import datetime

app = Flask(__name__)

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

if __name__ == '__main__':
    app.run()

