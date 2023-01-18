from os import path
from datetime import datetime
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from data_base.dbcore import Base
from settings import config
from models.users import Users
from models.points import  Points
from settings import utility


class Singleton(type):
    """
    Патерн Singleton предоставляет механизм создания одного
    и только одного объекта класса,
    и предоставление к нему глобальную точку доступа.
    """

    def __init__(cls, name, bases, attrs, **kwargs):
        super().__init__(name, bases, attrs)
        cls.__instance = None

    def __call__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__call__(*args, **kwargs)
        return cls.__instance


class DBManager(metaclass=Singleton):
    """ 
    Класс менеджер для работы с БД
    """

    def __init__(self):
        """
        Инициализация сессии и подключения к БД
        """
        self.engine = create_engine(config.DATABASE, connect_args={'check_same_thread': False})
        session = sessionmaker(bind=self.engine, autocommit=False, autoflush=False)
        self._session = scoped_session(session)
        if not path.isfile(config.DATABASE):
            Base.metadata.create_all(self.engine)

    def select_all_users(self):
        """
        Возвращает список зарегистрированных пользователей
        """
        users = self._session.query(Users).all()
        self.close()
        return users

    def select_user(self, user_id):
        """
        Возвращает пользователя
        :return:
        """
        user = self._session.query(Users).filter_by(user_id=user_id).all()
        self.close()
        return user

    def select_user_name(self, user_id):
        user = self._session.query(Users).filter_by(user_id=user_id).all()
        self.close()
        user_name = f'{user[0].first_name} {user[0].last_name}'
        return user_name

    def add_user(self, user_id, user_name):
        """
        Создаем пользователя по user_id и присваиваем состояние NAME
        :param user_name:
        :param user_id:
        :return:
        """
        user = Users(user_id=user_id, user_name=user_name, first_name=None, last_name=None, phone=None,
                     state=config.STATE['NAME'])
        self._session.add(user)
        self._session.commit()
        self.close()

    def add_point(self, name_point, author):
        """
        Добавляем точку в БД
        :param name_point:
        :param author:
        :return:
        """

        point = Points(name_point=name_point,
                       author=author)
        self._session.add(point)
        self._session.commit()
        self.close()

    def select_temp_point_user(self, user_id):
        """
        Возвращает временную/добавляемую точку пользователя
        :param user_id:
        :return:
        """
        point_temp = self._session.query(Users.temp_point).filter_by(user_id=user_id).all()
        # print(f'временная точка {point_temp[0][0]}')
        self.close()
        return point_temp[0][0]

    def updata_point(self, name_point, data):
        """
        Изменение/добавление данных о точке
        :param name_point:
        :param data:
        :return:
        """
        self._session.query(Points).filter_by(name_point=name_point).update(data)
        self._session.commit()
        self.close()

    def select_all_point(self):
        all_point = self._session.query(Points.name_point).all()
        self.close()
        return utility.convert(all_point)

    def select_point(self, name):
        """
        Метод возвращает точку из БД
        :param name:
        :return:
        """
        point = self._session.query(Points).filter_by(name_point=name).first()
        self.close()
        return point

    def state_user(self, user_id):
        """
        Метод возвращает состояние пользователя
        """
        #print('ss')
        state_user = self._session.query(Users.state).filter_by(user_id=user_id).first()
        # state = state_user[0]
        if state_user is None:
            return None
        else:
            return state_user[0]

    def update_user(self, user_id, data):
        """
        Обновление данных пользователя
        :param user_id:
        :param data:
        :return:
        """
        self._session.query(Users).filter_by(user_id=user_id).update(data)
        self._session.commit()
        self.close()

    def update_state_user(self, user_id, state):
        """
        Метод изменяет состояние пользователей
        """
        self._session.query(Users).filter_by(user_id=user_id).update({'state': state})
        self._session.commit()
        self.close()

    def download_points(self, data, author):
        """
        Загрузка точек в базу данных
        :param data: каталог точек
        :param author: автор кто загрузил
        :return:
        """
        # all_point = self.select_all_point()
        l = []
        for count, name_point in enumerate(data):
            print(count)
            if name_point not in self.select_all_point():
                data_point = data[name_point]
                point = Points(name_point=str(name_point).lower(),
                               x_coordinate=data_point['x_coordinate'],
                               y_coordinate=data_point['y_coordinate'],
                               h_coordinate=data_point['h_coordinate'],
                               author=author)
                l.append(point)
        self._session.add_all(l)
        self._session.commit()
        self.close()

    def del_point(self, name):
        n = self._session.query(Points).filter_by(name_point=name).one()
        self._session.delete(n)
        self._session.commit()
        self.close()

    def close(self):
        """ Закрывает сесию """
        self._session.close()
