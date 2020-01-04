"""page 341"""


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
    with UseDatabase(db_config) as cursor:
        _SQL = '''insert into log
                   (phrase, letters, ip, browser_string, results)
                  values
                   (%s, %s, %s, %s, %s)'''
        cursor.execute(_SQL, (req.form['phrase'], req.form['letters'],
                              req.remote_addr, req.user_agent.browser, res))
