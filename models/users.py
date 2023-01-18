# компоненты библиотеки для описания структуры таблицы
from sqlalchemy import Column, String, Integer, ForeignKey
from data_base.dbcore import Base


class Users(Base):
    """
    Класс для создания таблицы "Пользователи",
    основан на декларативном стиле SQLAlchemy
    """
    # название таблицы
    __tablename__ = 'users'

    # поля таблицы
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer)
    user_name = Column(String)
    first_name = Column(String)  # имя
    surname = Column(String)  # фамилия
    patronymic = Column(String)  # отчество
    phone = Column(String)
    specialization = Column(Integer, ForeignKey('orientation_type.id'))
    service_number = Column(String)  # табельный номер
    state = Column(String)

    def __repr__(self):
        """
        Метод возвращает формальное строковое представление указанного объекта
        """
        return f'{self.user_id, self.user_name, self.first_name, self.last_name, self.phone, self.state}'


class Specialization(Base):
    """
    Класс для создания таблицы "Должность"
    """
    # название таблицы
    __tablename__ = 'specialization'

    # поля таблицы
    id = Column(Integer, primary_key=True)
    name_specialization = Column(String)
