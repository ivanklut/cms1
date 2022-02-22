from model import field
"""
Здесь определяются операционные сущности.
Операционная сущность - это информационное отражение сущности
предметной области пользователя сервиса, т.е. объекты в бизнес-процессах.
Например: Новость, Статья, Задача, Товар, Заказ.
Они состоят из полей.
"""


class Entity:
    """
    Базовый класс для создания операционных сущностей.
    """
    def __init__(self):
        pass


class Article(Entity):
    """ Операционная сущность Статья """
    title = field.String(
        field_name='Название статьи',
        value=None,
        size=200,
        nullable=False,)
    content = field.Text(
        field_name='Текст статьи',
        value=None,
        size=9000,)

    def __init__(self, title, content,):
        super().__init__()
        self.title.value = title
        self.content.value = content


class News(Entity):
    """ Операционная сущность Новость """
    title = field.String(
        field_name='Название статьи',
        value=None,
        size=120,
        nullable=False, )
    content = field.Text(
        field_name='Текст статьи',
        value=None,
        size=2000, )
    image = field.Img(
        field_name='Картинка для анонса',
        value=None,  # id изображения в файловой системе
        img_title=None,
        default_value='/img/n.jpg',
        valid_file_extension='jpg',)

    def __init__(self, title, content, image, img_title):
        super().__init__()
        self.title.value = title
        self.content = content
        self.image = image
        self.img_title = img_title
