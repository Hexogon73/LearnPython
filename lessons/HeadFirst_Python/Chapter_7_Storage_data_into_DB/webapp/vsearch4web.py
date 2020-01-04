# -*- coding: utf-8 -*-
import mysql.connector
from flask import Flask, render_template, request, escape

from lessons.HeadFirst_Python.Chapter_4_Functions_and_modules.Modules.vsearch import search4letters

app = Flask(__name__)


def log_request(req: 'flask_request', res: str) -> None:
    """Журналирует веб-запрос и возвращает результаты

    :param req: запрос
    :param res: ответ
    """
    db_config = {'host': '127.0.0.1',
                 'user': 'vsearch',
                 'password': 'vsearchpasswd',
                 'database': 'vsearchlogDB',
                 }
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()
    _SQL = '''insert into log
               (phrase, letters, ip, browser_string, results)
              values
               (%s, %s, %s, %s, %s)'''
    cursor.execute(_SQL, (req.form['phrase'], req.form['letters'], req.remote_addr, req.user_agent.browser, res))
    conn.commit()
    cursor.close()
    conn.close()


@app.route('/search4', methods=['POST'])
def do_search() -> 'html':
    title = 'Here are your result:'
    phrase = request.form['phrase']
    letters = request.form['letters']
    results = str(search4letters(phrase, letters))
    log_request(request, results)
    return render_template('results.html',
                           the_title=title,
                           the_phrase=phrase,
                           the_letters=letters,
                           the_results=results, )


@app.route('/')
@app.route('/entry')
def entry_page() -> 'html':
    return render_template('entry.html',
                           the_title='Welcome to search4letters on the web!')


@app.route('/viewlog')
def view_the_log() -> str:
    with open('vsearch.log', 'r') as log:
        contents = [escape(line).split('|') for line in log.readlines()]
    titles = ('Form Data', 'Remote_addr', 'User_agent', 'Results')
    return render_template('viewlog.html',
                           the_title='View Log',
                           the_row_titles=titles,
                           the_data=contents, )


if __name__ == '__main__':
    app.run(debug=True)
