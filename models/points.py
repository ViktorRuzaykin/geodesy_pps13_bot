# компоненты библиотеки для описания структуры таблицы
from sqlalchemy import Column, String, Integer, Boolean, Float
from data_base.dbcore import Base


class Points(Base):
    """
    Класс для создания таблицы "Точки",
    основан на декларативном стиле SQLAlchemy
    """
    # название таблицы
    __tablename__ = 'points'

    # поля таблицы
    id = Column(Integer, primary_key=True)
    name_point = Column(String)
    x_coordinate = Column(Float)
    y_coordinate = Column(Float)
    h_coordinate = Column(Float)
    image_path = Column(String)
    description = Column(String)
    author = Column(String)

    def __repr__(self):
        """
        Метод возвращает формальное строковое представление указанного объекта
        """
        return f'{self.id, self.name_point, self.x_coordinate, self.y_coordinate, self.h_coordinate, self.image_path, self.description, self.author}'

    @property
    def serialize(self):
        return {
            'id': self.id,
            'name_point': self.name_point,
            'x_coordinate': self.x_coordinate,
            'y_coordinate': self.y_coordinate,
            'h_coordinate': self.h_coordinate,
            'image_path': self.image_path,
            'description': self.description,
            'author': self.author,
        }
