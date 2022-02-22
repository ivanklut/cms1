from model import entity, idb


def main():
    d = {'title': "Это третья статья",
         'content': "Это текст третей статьи"}
    art3 = entity.Article(**d)
    print(art3)
    idb.save_new_entity(art3)

    '''
    # явно передаем значения полей
    art1 = ent.Article(
            title="Это первая статья",
            content="Это текст первой статьи",)
    art1.print_entity()
    art1.save()

    # передаем значения полей словарем
    d = {'title': "Это вторая статья",
         'content': "Это текст второй статьи"}
    art2 = ent.Article(**d)
    art2.save()
    art2.print_entity()
    '''


if __name__ == '__main__':
    # Инициализация системы
    idb.create_table_for_every_entity()
    # Запуск системы
    main()
