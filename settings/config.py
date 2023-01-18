import os
from emoji import emojize


NAME_DB = 'geodesy_pp13.db'
# версия приложения
# VERSION = '0.0.1'
# автор приложния
# AUTHOR = 'User'

# родительская директория
# BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# путь до базы данных
DATABASE = os.path.join('sqlite:///' + os.path.abspath(NAME_DB))

SRC_IMAGE = 'media/image'
# токен выдается при регистрации приложения
TOKEN = '5957927034:AAHK4tv8m5eU9UTWR0L24JmjC_o1vemI6iE'  # product
# TOKEN = '5863878331:AAHfa-Fxp4jbQVyS1XVn8pX-TaRMo163_v8' # testing

# кнопки управления
KEYBOARD = {
    'ADD_POINT': emojize('⊙Добавить точку'),
    'SEARCH': emojize('🔍Найти точку'),
    'ALL_POINTS': emojize('📋Весь список точек'),
    'BACK': emojize('🔙Назад'),
    'SKIP': emojize('▶Пропустить'),
    'YES': emojize('✅Да'),
    'NEGATIVE': emojize('❌Нет'),
    'DOWNLOAD_POINT': emojize('⬇Загрузить точки'),
    'DELETE_POINT': emojize('❌Удалить'),
    'EDIT_POINT': emojize('📝Поправить'),
    'EDIT_COORDINATE': emojize('🌐Координаты'),
    'EDIT_NAME': emojize('Имя'),
    'EDIT_IMAGE': emojize('📸Фото'),
    'EDIT_DESCRIPTION': emojize('📋Описание'),

}

# состояние пользователей
STATE = {
    'NAME': 'NAME',
    'PHONE': 'PHONE',
    'START_MENU': 'START_MENU',
    'STEP_1': 'STEP_1',
    'STEP_2': 'STEP_2',
    'STEP_3': 'STEP_3',
    'STEP_4': 'STEP_4',
    'SEARCH': 'SEARCH',
    'DOWNLOAD_POINT': 'DOWNLOAD_POINT',
    'EDIT_POINT': 'EDIT_POINT',
    'DELETE_POINT': 'DELETE_POINT',
    'EDIT_NAME': 'EDIT_NAME',
    'EDIT_COORDINATE': 'EDIT_COORDINATE',
    'EDIT_IMAGE': 'EDIT_IMAGE',
    'EDIT_DESCRIPTION': 'EDIT_DESCRIPTION',
}
