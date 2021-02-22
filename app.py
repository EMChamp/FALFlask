from flask import Flask
from database_helpers import database_helpers
app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/get_challenger_league')
def get_challengers_league():
    dh = database_helpers()
    return dh.return_challenger_league()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
