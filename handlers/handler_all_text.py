import os

from handlers.handler import Handler
from settings import config
from settings.message import MESSAGE
from settings import utility
import re


class HandlersAllText(Handler):
    """
    Класс обрабатывает сообщения от пользователя при добавлении новой точки
    """

    def __init__(self, bot):
        super().__init__(bot)

    def pressed_btn_add_point(self, message):
        id_user = message.from_user.id
        self.BD.update_state_user(id_user, config.STATE['STEP_1'])
        self.bot.send_message(message.chat.id, MESSAGE['add_step_1'],
                              parse_mode="HTML", reply_markup=self.keybords.remove_menu())

    def pressed_btn_search(self, message):
        id_user = message.from_user.id
        self.BD.update_state_user(id_user, config.STATE['SEARCH'])
        self.bot.send_message(message.chat.id, MESSAGE['search'],
                              parse_mode="HTML", reply_markup=self.keybords.remove_menu())

    def pressed_btn_all_point(self, message):
        count_point = len(self.BD.select_all_point())
        self.bot.send_message(message.chat.id, MESSAGE['error_all_point'].format(count_point),
                              parse_mode="HTML",
                              reply_markup=self.keybords.start_menu())

    def pressed_btn_download(self, message):
        id_user = message.from_user.id
        self.BD.update_state_user(id_user, config.STATE['DOWNLOAD_POINT'])
        self.bot.send_message(message.chat.id, MESSAGE['download_point'],
                              parse_mode="HTML", reply_markup=self.keybords.remove_menu())


    def download_doc(self, message):
        """
        Загрузка документа
        :param message:document
        :return:
        """
        file_info = self.bot.get_file(message.document.file_id)
        downloaded_file = self.bot.download_file(file_info.file_path)
        src = message.document.file_name
        with open(src, 'wb') as new_file:
            new_file.write(downloaded_file)

    def handle(self):
        # обработчик(декоратор) сообщений

        @self.bot.message_handler(
            func=lambda message: (self.BD.state_user(message.from_user.id)) == config.STATE['START_MENU'])
        def handle(message):

            # ********** основное меню ********** #
            group_to_method = {
                config.KEYBOARD['ADD_POINT']: self.pressed_btn_add_point,
                config.KEYBOARD['SEARCH']: self.pressed_btn_search,
                config.KEYBOARD['ALL_POINTS']: self.pressed_btn_all_point,
                config.KEYBOARD['DOWNLOAD_POINT']: self.pressed_btn_download,
            }
            try:
                group_to_method[message.text](message)
            except KeyError:
                pass

        @self.bot.message_handler(
            func=lambda message: (self.BD.state_user(message.from_user.id)) == config.STATE['DOWNLOAD_POINT'], content_types=['document'])
        def download_catalog(message):
            user_id = message.from_user.id
            author = self.BD.select_user_name(user_id=user_id)
            # print(message.document)
            self.download_doc(message=message)
            try:
                name_file = message.document.file_name
                data = utility.download_catalog_coordinates_bd(catalog_file=name_file, delimiter=',')
                self.BD.download_points(data=data, author=author)
                self.bot.send_message(message.chat.id, 'Точки загружены!', reply_markup=self.keybords.start_menu())
                self.BD.update_state_user(user_id=user_id, state=config.STATE['START_MENU'])
                os.remove(name_file)

            except:
                return self.bot.send_message(message.chat.id, 'Ошибка чтения файла!')

        @self.bot.message_handler(
            func=lambda message: (self.BD.state_user(message.from_user.id)) == config.STATE['EDIT_NAME'])
        def pressed_btn_edit_name(message):
            user_id = message.from_user.id
            new_name_point = message.text.lower()
            if new_name_point in self.BD.select_all_point():
                return self.bot.send_message(message.chat.id, MESSAGE['error_step_1'], parse_mode="HTML")
            name_point_temp = self.BD.select_temp_point_user(user_id=user_id)
            data = {'name_point': new_name_point}
            self.BD.updata_point(name_point=name_point_temp, data=data)


        @self.bot.message_handler(
            func=lambda message: (self.BD.state_user(message.from_user.id)) == config.STATE['EDIT_COORDINATE'])
        def pressed_btn_edit_coordinate(message):
            pass

        @self.bot.message_handler(
            func=lambda message: (self.BD.state_user(message.from_user.id)) == config.STATE['EDIT_IMAGE'])
        def pressed_btn_download_edit_image(message):
            pass

        @self.bot.message_handler(
            func=lambda message: (self.BD.state_user(message.from_user.id)) == config.STATE['EDIT_DESCRIPTION'])
        def pressed_btn_edit_description(message):
            pass
