"""page 326"""
import mysql.connector

db_config = {'host': '127.0.0.1',
             'user': 'vsearch',
             'password': 'vsearchpasswd',
             'database': 'vsearchlogDB',
             }
conn = mysql.connector.connect(**db_config)
cursor = conn.cursor()

cursor.close()
conn.close()
