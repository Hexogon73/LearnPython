"""page 245"""

from flask import Flask
from lessons.HeadFirst_Python.Chapter_4_Functions_and_modules.Modules.vsearch import search4letters

app = Flask(__name__)


@app.route('/')
def hello() -> str:
    return 'Hello world from Flask!'


@app.route('/search4')
def do_search() -> str:
    return str(search4letters('life, the universe, and everything', 'eiru,!'))


app.run()
