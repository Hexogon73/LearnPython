# -*- coding: utf-8 -*-
from flask import Flask, render_template, request, session

from lessons.HeadFirst_Python.Chapter_4_Functions_and_modules.Modules.vsearch import search4letters
from .DBcm import UseDatabase
from .checker import check_logged_in

app = Flask(__name__)
app.config['db_config'] = {'host': '127.0.0.1',
                           'user': 'vsearch',
                           'password': 'vsearchpasswd',
                           'database': 'vsearchlogDB', }

app.secret_key = 'YouWillNeverGuessMySecretKey'


@app.route('/login')
def do_login() -> str:
    session['logged_in'] = True
    return 'You are now logged in'


@app.route('/logout')
def do_logout() -> str:
    session.pop('logged_in')
    return 'You are now logged out'


def log_request(req: 'flask_request', res: str) -> None:
    """Журналирует веб-запрос и возвращает результаты

    :param req: запрос
    :param res: ответ
    """
    with UseDatabase(app.config['db_config']) as cursor:
        _SQL = '''insert into log
                  (phrase, letters, ip, browser_string, results)
                  values
                  (%s, %s, %s, %s, %s)'''
        cursor.execute(_SQL, (req.form['phrase'], req.form['letters'],
                              req.remote_addr, req.user_agent.browser, res))


@app.route('/search4', methods=['POST'])
def do_search() -> 'html':
    """Извлекает данные из запроса; выполняет поиск; возвращает результаты"""
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
    """Выводит HTML-форму"""
    return render_template('entry.html',
                           the_title='Welcome to search4letters on the web!')


@app.route('/viewlog')
@check_logged_in
def view_the_log() -> str:
    """Выводит содержимое файла журнала в виде HTML-таблицы"""
    with UseDatabase(app.config['db_config']) as cursor:
        _SQL = '''select phrase, letters, ip, browser_string, results
                  from log'''
        cursor.execute(_SQL)
        contents = cursor.fetchall()
    titles = ('Phrase', 'Letters', 'Remote_addr', 'User_agent', 'Results')
    return render_template('viewlog.html',
                           the_title='View Log',
                           the_row_titles=titles,
                           the_data=contents, )


if __name__ == '__main__':
    app.run(debug=True)
