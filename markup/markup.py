# импортируем специальные типы телеграм бота для создания элементов интерфейса
from telebot.types import KeyboardButton, ReplyKeyboardMarkup, \
    ReplyKeyboardRemove, InlineKeyboardMarkup, InlineKeyboardButton
# импортируем настройки и утилиты
from settings import config
# импортируем класс-менеджер для работы с библиотекой
from data_base.dbalchemy import DBManager
from telebot import types


class Keyboards:
    """
    Класс Keyboards предназначен для создания и разметки интерфейса бота
    """

    # инициализация разметки

    def __init__(self):
        self.markup = None
        # инициализируем менеджер для работы с БД
        self.BD = DBManager()

    @staticmethod
    def set_btn(name):
        """
        Создает и возвращает кнопку по входным параметрам
        """
        return KeyboardButton(config.KEYBOARD[name])

    @staticmethod
    def set_inline_btn(name):
        """
        Создает и возвращает инлайн кнопку по входным параметрам
        """
        return InlineKeyboardButton(str(name), callback_data=str(name))

    @staticmethod
    def set_inline_btn_2(name_name):
        return [InlineKeyboardButton(str(name), callback_data=str(name)) for name in name_name]

    @staticmethod
    def remove_menu():
        """
        Удаляет кнопки
        """
        return ReplyKeyboardRemove()

    def start_menu(self):
        """
        Создает разметку кнопок при старте бота
        """
        self.markup = ReplyKeyboardMarkup(True, True)
        itm_btn_1 = self.set_btn('ADD_POINT')
        itm_btn_2 = self.set_btn('SEARCH')
        itm_btn_3 = self.set_btn('ALL_POINTS')
        itm_btn_4 = self.set_btn('DOWNLOAD_POINT')

        # рассположение кнопок в меню
        self.markup.row(itm_btn_1, itm_btn_2)
        self.markup.row(itm_btn_3, itm_btn_4)
        return self.markup

    def set_select_all_point(self, points):
        """
        Создает разметку инлайн-кнопок всех точек
        """
        self.markup = InlineKeyboardMarkup(row_width=1)
        if len(points) > 4:
            new_points = [[i, j, h, g] for i, j, h, g in zip(points[0::4], points[1::4], points[2::4], points[3::4])]
            new_points_tmp = [j for i in new_points for j in i]
            l = list(set(points) - set(new_points_tmp))
            new_points.append(l)
            for itm in new_points:
                if len(itm) == 4:
                    self.markup.row(self.set_inline_btn(itm[0]),
                                    self.set_inline_btn(itm[1]),
                                    self.set_inline_btn(itm[2]),
                                    self.set_inline_btn(itm[3]))
                else:
                    for btn in itm:
                        self.markup.add(self.set_inline_btn(btn))
        else:
            for itm in points:
                self.markup.add(self.set_inline_btn(itm))
        return self.markup

    def btn_skip(self):
        """
        Создает inline кнопку 'Пропустить'
        """
        self.markup = InlineKeyboardMarkup(row_width=1)
        btn1 = self.set_inline_btn(config.KEYBOARD['SKIP'])
        self.markup.add(btn1)
        return self.markup

    def set_step(self):
        """
        Создает инлайн кнопки удаления и редактирования точки
        """
        self.markup = InlineKeyboardMarkup(row_width=1)
        btn1 = self.set_inline_btn(config.KEYBOARD['EDIT_POINT'])
        btn2 = self.set_inline_btn(config.KEYBOARD['DELETE_POINT'])
        self.markup.row(btn1, btn2)
        return self.markup

    def confirmation_point(self):
        self.markup = InlineKeyboardMarkup(row_width=1)
        btn1 = self.set_inline_btn(config.KEYBOARD['YES'])
        btn2 = self.set_inline_btn(config.KEYBOARD['NEGATIVE'])
        self.markup.row(btn1, btn2)
        return self.markup

    def edit_point(self):
        """
        Подтверждение удаление точки
        """
        self.markup = InlineKeyboardMarkup(row_width=1)
        btn1 = self.set_inline_btn(config.KEYBOARD['EDIT_NAME'])
        btn2 = self.set_inline_btn(config.KEYBOARD['EDIT_COORDINATE'])
        btn3 = self.set_inline_btn(config.KEYBOARD['EDIT_IMAGE'])
        btn4 = self.set_inline_btn(config.KEYBOARD['EDIT_DESCRIPTION'])
        self.markup.row(btn1, btn3)
        self.markup.row(btn2, btn4)
        return self.markup

