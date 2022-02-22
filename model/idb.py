"""
Интерфейс хранилища
"""
from model import entity
#from repository import sqlite_adapter as db
import importlib

# print(db)
CURRENT_DATABASE = 'repository.sqlite_adapter'
# db1 = __import__('repository.sqlite_adapter')
db = importlib.import_module(CURRENT_DATABASE)
print(db)


def create_table_for_every_entity():
    """
    Сканируем параметры операционных сущностей и
    передаем в адаптер БД с целью создания таблиц.
    Для каждой сущности отдельная таблица. Большие поля храним отдельно.
    """
    entity_list = entity.Entity.__subclasses__()
    for ent in entity_list:
        entity_name = ent.__name__.lower()
        field_list = []
        for attr in ent.__dict__:
            field_description = {attr: {}}
            if '__' not in attr:
                # print(f'атрибут: {attr}')
                # print(f'Пример: {getattr(ent, attr).__dict__}')
                field_description[attr] = getattr(ent, attr).__dict__
                # print(field_description)
                field_list.append(field_description)
        db.create_table(entity_name, field_list)
        # print('----------------------\n')


def save_new_entity(ent):
    """
    Передаем адаптеру БД название таблицы (имя сущности),
    кортеж со списком полей и кортеж их значений.
    :param ent: Экземпляр класса сущности
    :return:
    """
    entity_name = ent.__class__.__name__.lower()
    print(ent)
    field_description = {}
    for attr in ent.__dir__():
        if '__' not in attr:
            field_description[attr] = getattr(ent, attr).value
            # print(f'field_description {field_description}')
    fields = tuple(field_description.keys())
    # print(f'--{fields}')
    values = tuple(field_description.values())
    # print(f'--{values}')
    db.insert_entity(table_name=entity_name, fields=fields, values=values)




if __name__ == "__main__":
    # create_table_for_every_entity()
    d = {'title': "Это вторая статья",
         'content': "Это текст второй статьи"}
    art2 = entity.Article(**d)
    save_new_entity(art2)
