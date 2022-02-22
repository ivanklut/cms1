"""
Адаптер к БД SQLite
"""
import sqlite3
import os.path

CUR_DIR = os.path.dirname(__file__)
DB_NAME = 'model_data'
'''
Примечание: 
connection - представляет реальную базу данных на диске компьютера.
cursor — это объект в памяти с методами для проведения SQL команд или 
хранения итогов их выполнения.
'''
# todo: разобраться как правильно указывать пути

def create_table(table_name, field_list):
    """
    Создает таблицу по названию и списку полей
    :param table_name: текст
    :param fields: список полей
    :return:
    """
    # print(f'Получил:{table_name}, {fields}')
    # todo: распарсить fields и вставить в SQL-запрос
    with sqlite3.connect(f'{CUR_DIR}\\{DB_NAME}.db') as conn:
        cur = conn.cursor()
        req = (
            f'CREATE TABLE IF NOT EXISTS {table_name}('
            f'ent_id INTEGER PRIMARY KEY AUTOINCREMENT,'
            f'title TEXT NOT NULL,'
            f'content TEXT'
            f')'
        )
        cur.execute(req)


def drop_db(table_name):
    """
    Удаляет указанную таблицу
    """
    with sqlite3.connect(f'{CUR_DIR}\\{DB_NAME}.db') as conn:
        cur = conn.cursor()
        req = f'DROP TABLE IF EXISTS {table_name}'
        cur.execute(req)


def exe_db_req(req):
    """
    Коннектится к базе и исполняет запрос
    """
    # print(f'---{table_name}|{query}|{params}')
    with sqlite3.connect(f'{CUR_DIR}\\{DB_NAME}.db') as conn:
        cur = conn.cursor()
        cur.execute(req)
        response = cur.fetchall()
        print(response)
        return response


def insert_entity(table_name, fields, values):
    print(table_name, fields, values)
    req = (
        f'INSERT INTO {table_name} {fields} VALUES {values}'
    )
    print(req)
    exe_db_req(req)


def select_x(table_name, ent_id):
    req = (
        f'SELECT content, title '
        f'FROM {table_name} '
        f'WHERE title > 1 '
        f'ORDER BY title ASC '
        f'LIMIT 2 OFFSET 1'
    )
    response = exe_db_req(req)
    return response

def select_bu_id(table_name, ent_id):
    pass

if __name__ == "__main__":
    insert_entity(table_name='article',
                  fields=('title', 'content'),
                  values=('ttt111', 'Содержимое статьи1'))
    select_x(table_name='article', ent_id='1')
