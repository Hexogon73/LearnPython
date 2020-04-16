# -*- coding: utf-8 -*-
from threading import Thread
from time import sleep

from flask import Flask, render_template, request, session
from flask import copy_current_request_context

from .DBcm import UseDatabase, ConnectionError, CredentialsError, SQLError
from .checker import check_logged_in
from .vsearch import search4letters

app = Flask(__name__)
app.config['db_config'] = {'host': '127.0.0.1',
                           'user': 'vsearch',
                           'password': 'vsearchpasswd',
                           'database': 'vsearchlogDB', }


@app.route('/login')
def do_login() -> str:
    session['logged_in'] = True
    return 'You are now logged in'


@app.route('/logout')
def do_logout() -> str:
    session.pop('logged_in')
    return 'You are now logged out'


@app.route('/search4', methods=['POST'])
def do_search() -> 'html':
    """Извлекает данные из запроса; выполняет поиск; возвращает результаты"""

    @copy_current_request_context
    def log_request(req: 'flask_request', res: str) -> None:
        """Журналирует веб-запрос и возвращает результаты

        :param req: запрос
        :param res: ответ
        """
        try:
            sleep(15)  # This makes log_request really slow...
            with UseDatabase(app.config['db_config']) as cursor:
                _SQL = '''insert into log
                          (phrase, letters, ip, browser_string, results)
                          values
                          (%s, %s, %s, %s, %s)'''
                cursor.execute(_SQL, (req.form['phrase'], req.form['letters'],
                                      req.remote_addr, req.user_agent.browser, res))
        except ConnectionError as _err:
            print('Is your database switched on? Error:', str(_err))
        except CredentialsError as _err:
            print('User-id/Password issues. Error:', str(_err))
        except SQLError as _err:
            print('Is you query correct? Error:', str(_err))
        except Exception as _err:
            print('Something went wrong:', str(_err))

    phrase = request.form['phrase']
    letters = request.form['letters']
    title = 'Here are your result:'
    results = str(search4letters(phrase, letters))
    try:
        t = Thread(target=log_request, args=(request, results))
        t.start()
    except Exception as err:
        print('***** Logging failed with this error:', str(err))
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
    try:
        with UseDatabase(app.config['db_config']) as cursor:
            _SQL = '''select phrase, letters, ip, browser_string, results
                      from log'''
            cursor.execute(_SQL)
            contents = cursor.fetchall()
        # raise Exception('Some unknown exception')
        titles = ('Phrase', 'Letters', 'Remote_addr', 'User_agent', 'Results')
        return render_template('viewlog.html',
                               the_title='View Log',
                               the_row_titles=titles,
                               the_data=contents, )
    except ConnectionError as err:
        print('Is your database switched on? Error:', str(err))
    except CredentialsError as err:
        print('User-id/Password issues. Error:', str(err))
    except SQLError as err:
        print('Is you query correct? Error:', str(err))
    except Exception as err:
        print('Something went wrong:', str(err))
    return 'Error'


app.secret_key = 'YouWillNeverGuessMySecretKey'

if __name__ == '__main__':
    app.run(debug=True)
