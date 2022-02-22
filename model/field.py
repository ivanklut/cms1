# from abc import ABC, abstractmethod
"""
Элементы (поля) использующиеся при создании операционных сущностей.
"""


class Field:
    """Базовый класс для элементов сущностей"""
    def __init__(self, field_name, value, size, default_value=None, nullable=True,):
        self.field_name = field_name
        self.value = value
        self.size = size
        self.default_value = default_value
        self.nullable = nullable
        self.value_type = None


class String(Field):
    """Строковое поле"""
    aaa = 'sss'
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.value_type = 'text'


class Text(Field):
    """Текстовое поле"""
    def __init__(self, field_name, value, size=8000, default_value=None,):
        super().__init__(field_name, value, size, default_value)
        self.value_type = 'str'
        # как указать неограничено? или просто поставить большое число?
        # При превышении,например, 255 символов,хранить в отдельной таблице


class Img(Field):
    """
    Поле с изображениями.
    size=0 - означает неограниченное значение, как по другому?
    """
    def __init__(self, field_name, value, img_title,
                 default_value=None, valid_file_extension='jpg',):
        super().__init__(field_name, value, default_value)
        # self.value это url
        self.size = 250
        self.value_type = 'int'
        self.valid_file_extension = valid_file_extension
        self.img_title = img_title
