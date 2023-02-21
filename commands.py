import pathlib
from pathlib import Path

import sqlite3
from sqlite3 import Error

from datetime import datetime


def create_connection():    #создаем подключение
    path = create_path('base')
    connection = None
    try:
        connection = sqlite3.connect(path)
        print(f"Connection...")
    except Error as e:
        print(f"Error\n{e}")

    return connection


def create_path(name):     #получаем путь
    name += ".sqlite"
    path = Path(pathlib.Path().absolute(), name)
    return path


def execute_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
    except Error as e:
        print(f"Error\n{e}")


def execute_queries(connection, query, args):
    cursor = connection.cursor()
    try:
        cursor.execute(query, args)
        connection.commit()
    except Error as e:
        print(f"Error\n{e}")


def execute_read_query(connection, query):
    cursor = connection.cursor()
    result = None
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except Error as e:
        print(f"Error\n{e}")


def print_sql(result):
    print('_'*50)
    for i in result:
        for j in i:
            print(j, '|  ', end='')
        print('\n', '-' * 50, sep='')





#Описание запросов SQL
create_users_table ="""
CREATE TABLE IF NOT EXISTS user (
    user_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(1024),
    date_birth DATE,
    sex VARCHAR(6)
    );
"""

create_user = """
   INSERT INTO
       user (name, date_birth, sex)
   VALUES
       (?,?,?);
   """


def create_many_users(users):

    many_users = f"""
       INSERT INTO
           user (name, date_birth, sex)
       VALUES
           {users};
       """
    return many_users


filter_F = """
SELECT name, date_birth, sex
FROM user
WHERE sex = 'male' AND (name LIKE 'F%')
"""


current_datetime = str(datetime.now()).split()[0]

select_all = f"""
SELECT name, date_birth, sex, CAST((JULIANDAY("{current_datetime}") - JULIANDAY(date_birth))/365 AS INTEGER) AS age
FROM user
GROUP BY name, date_birth
ORDER BY name;
"""


