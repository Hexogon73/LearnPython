"""page 327, 328, 329"""
import mysql.connector

db_config = {'host': '127.0.0.1',
             'user': 'vsearch',
             'password': 'vsearchpasswd',
             'database': 'vsearchlogDB',
             }
conn = mysql.connector.connect(**db_config)
cursor = conn.cursor()

_SQL = '''show tables'''
cursor.execute(_SQL)
res = cursor.fetchall()
print(res)

###
_SQL = '''describe log'''
cursor.execute(_SQL)
res = cursor.fetchall()
for row in res:
    print(row)

cursor.close()
conn.close()
