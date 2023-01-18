# компоненты библиотеки для описания структуры таблицы
from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship, backref
from data_base.dbcore import Base


class DocExecutive(Base):
    """
    Класс для создания таблицы "Исполнительная документация",
    основан на декларативном стиле SQLAlchemy
    """
    # название таблицы
    __tablename__ = 'executive_documentation'

    # поля таблицы
    id = Column(Integer, primary_key=True)
    orientation = Column(String)  # направление
    code = Column(String)  # шифр проекта
    position = Column(String)  # номер позиции/объект
    project_section = Column(String)  # раздел проекта
    number_sheet = Column(String)  # номер листа
    type_work = Column(String)  # конструктив
    location = Column(String)  # пикетаж
    status_doc = Column(Integer,  ForeignKey('status_doc.id'))  # статус ИС
    scheme = Column(String)  # схема
    comment = Column(String)  # примечание/комментарий
    author = Column(String)  # автор ИС

    def __repr__(self):
        """
        Метод возвращает формальное строковое представление указанного объекта
        """
        return f'{self.id, self.author}'


class OrientationType(Base):
    """
    Класс для создания таблицы "Направления работ",
    основан на декларативном стиле SQLAlchemy
    """
    # название таблицы
    __tablename__ = 'orientation_type'

    # поля таблицы
    id = Column(Integer, primary_key=True)
    name_orientation = Column(String)  # направление

    def __repr__(self):
        """
        Метод возвращает формальное строковое представление указанного объекта
        """
        return f'{self.id, self.author}'


class Code(Base):
    """
    Класс для создания таблицы "Шифр"
    """
    # название таблицы
    __tablename__ = 'code'

    # поля таблицы
    id = Column(Integer, primary_key=True)
    name_code = Column(String)  # имя шифра
    orientation_type_id = Column(Integer, ForeignKey('orientation_type.id'))
    orientation_type = relationship(
        OrientationType,
        backref=backref('code',
                        uselist=True,
                        cascade='delete,all'))


class Position(Base):
    """
    Класс для создания таблицы "Номер позиции/объект"
    """
    # название таблицы
    __tablename__ = 'position'

    # поля таблицы
    id = Column(Integer, primary_key=True)
    name_position = Column(String)  # позиция
    orientation_type_id = Column(Integer, ForeignKey('orientation_type.id'))
    orientation_type = relationship(
        OrientationType,
        backref=backref('position',
                        uselist=True,
                        cascade='delete,all'))


class ProjectSection(Base):
    """
    Класс для создания таблицы "Раздел проекта"
    """
    # название таблицы
    __tablename__ = 'project_section'

    # поля таблицы
    id = Column(Integer, primary_key=True)
    name_project_section = Column(String)  # раздел проекта
    orientation_type_id = Column(Integer, ForeignKey('orientation_type.id'))
    orientation_type = relationship(
        OrientationType,
        backref=backref('project_section',
                        uselist=True,
                        cascade='delete,all'))


class TypeWork(Base):
    """
    Класс для создания таблицы "Конструктив"(вид работ)
    """
    # название таблицы
    __tablename__ = 'type_work'

    # поля таблицы
    id = Column(Integer, primary_key=True)
    name_type_work = Column(String)  # имя конструктив
    orientation_type_id = Column(Integer, ForeignKey('orientation_type.id'))
    orientation_type = relationship(
        OrientationType,
        backref=backref('type_work',
                        uselist=True,
                        cascade='delete,all'))


class StatusDoc(Base):
    """
    Класс для создания таблицы "Статус ИД"
    """
    # название таблицы
    __tablename__ = 'status_doc'

    # поля таблицы
    id = Column(Integer, primary_key=True)
    name_status_doc = Column(String)  # статус схемы

