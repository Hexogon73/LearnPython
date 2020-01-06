"""page 383"""
from lessons.HeadFirst_Python.Chapter_9_With_DB.DBcm import UseDatabase

db_config = {'host': '127.0.0.1',
             'user': 'vsearch',
             'password': 'vsearchpasswd',
             'database': 'vsearchlogDB',
             }

with UseDatabase(db_config) as cursor:
    _SQL = '''show tables'''
    cursor.execute(_SQL)
    data = cursor.fetchall()

print(data)
