"""page 253, 259, 262, 268, 271"""

from flask import Flask, render_template, request, redirect
from vsearch import search4letters

app = Flask(__name__)


@app.route('/')
def hello() -> '302':
    return redirect('/entry')


@app.route('/search4', methods=['POST'])
def do_search() -> 'html':
    title = 'Here are your result:'
    phrase = request.form['phrase']
    letters = request.form['letters']
    results = str(search4letters(phrase, letters))
    return render_template('results.html',
                           the_title=title,
                           the_phrase=phrase,
                           the_letters=letters,
                           the_results=results, )


@app.route('/entry')
def entry_page() -> 'html':
    return render_template('entry.html',
                           the_title='Welcome to search4letters on the web!')


app.run(debug=True)
