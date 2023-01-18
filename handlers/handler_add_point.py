from handlers.handler import Handler
from settings import config
from settings.message import MESSAGE


class HandlersAddPoint(Handler):
    """
    Класс обрабатывает сообщения от пользователя при добавлении новой точки
    """

    def __init__(self, bot):
        super().__init__(bot)

    def send_request_tu_admin(self, message, card):
        """
        Отправка жалобы администрации. Если медиа нет, то отправляем текст.
        """
        if card['media']:
            photo = open(card['media'], 'rb')
            self.bot.send_photo(message.chat.id,
                                photo=photo,
                                caption=MESSAGE['complaint'].format(
                                    f'@{card["user_name"]}',
                                    card['full_name'],
                                    card['phone'],
                                    card['address'],
                                    card['description']
                                ), parse_mode="HTML")
        else:
            self.bot.send_message(message.chat.id,
                                  MESSAGE['complaint'].format(
                                      f'@{card["user_name"]}',
                                      card['full_name'],
                                      card['phone'],
                                      card['address'] if card['address'] else '-',
                                      card['description']
                                  ), parse_mode="HTML")

    @staticmethod
    def file_path(message, name_point, user_name):
        """
        Возвращает путь сохранения файла зависимости от типа файла
        """
        src = ''
        if message.content_type == 'photo':
            src = config.SRC + str(name_point) + '_' + str(user_name) + '.jpg'
        return src

    def download_photo(self, message, name_point, user_name):
        """
        Загрузка фото от пользователя
        """
        file_info = self.bot.get_file(message.photo[len(message.photo) - 1].file_id)
        downloaded_file = self.bot.download_file(file_info.file_path)
        src = config.SRC + str(name_point) + '_' + str(user_name) + '.jpg'
        with open(src, 'wb') as new_file:
            new_file.write(downloaded_file)

    def handle(self):
        # обработчик(декоратор) сообщений
        @self.bot.message_handler(
            func=lambda message: (self.BD.state_user(message.from_user.id)) == config.STATE['STEP_1'])
        def name_point(message):
            name_point = message.text.lower()
            if name_point in self.BD.select_all_point():
                return self.bot.send_message(message.chat.id, MESSAGE['error_step_1'], parse_mode="HTML")
            # print(name_point)
            user_id = message.from_user.id
            author = self.BD.select_user_name(user_id=user_id)
            self.BD.add_point(name_point=name_point, author=author)
            data = {
                'temp_point': name_point
            }
            self.BD.update_user(user_id=user_id, data=data)
            self.bot.send_message(message.chat.id, MESSAGE['add_step_2'], parse_mode="HTML")
            self.BD.update_state_user(user_id=user_id, state=config.STATE['STEP_2'])
            # self.BD.select_temp_point_user(user_id=user_id)

        @self.bot.message_handler(
            func=lambda message: (self.BD.state_user(message.from_user.id)) == config.STATE['STEP_2'])
        def coordinates_poit(message):
            user_id = message.from_user.id
            name_point_temp = self.BD.select_temp_point_user(user_id=user_id)
            coordinates = message.text.split(' ')
            if len(coordinates) != 3:
                print('ошибка в данных')
                return self.bot.send_message(message.chat.id, MESSAGE['error_step_2'], parse_mode="HTML")
            try:
                x, y, h = float(coordinates[0]), float(coordinates[1]), float(coordinates[2])
                data = {
                    'x_coordinate': x,
                    'y_coordinate': y,
                    'h_coordinate': h
                }
                self.BD.updata_point(name_point=name_point_temp, data=data)
                self.bot.send_message(message.chat.id, MESSAGE['add_step_3'], parse_mode="HTML",
                                      reply_markup=self.keybords.btn_skip())
                self.BD.update_state_user(user_id=user_id, state=config.STATE['STEP_3'])
            except ValueError:
                self.bot.send_message(message.chat.id, MESSAGE['error_step_2'], parse_mode="HTML")


        @self.bot.message_handler(content_types=['photo'])
        def photo_point(message):
            if message.media_group_id:
                return self.bot.send_message(message.chat.id, 'Должно быть одно фото!')
            if (self.BD.state_user(message.from_user.id)) == config.STATE['STEP_3']:
                user_id = message.from_user.id
                user_name = message.from_user.username
                name_point_temp = self.BD.select_temp_point_user(user_id=user_id)
                if message.content_type == 'photo':
                    self.download_photo(message, name_point_temp, user_name)
                    path = self.file_path(message, name_point_temp, user_name)
                    data = {'image_path': path}
                    self.BD.updata_point(name_point=name_point_temp, data=data)
                    self.bot.send_message(message.chat.id, MESSAGE['add_step_4'], parse_mode="HTML",
                                          reply_markup=self.keybords.btn_skip())
                    self.BD.update_state_user(user_id=user_id, state=config.STATE['STEP_4'])

        @self.bot.message_handler(
            func=lambda message: (self.BD.state_user(message.from_user.id)) == config.STATE['STEP_4'])
        def get_description(message):
            description_point = message.text
            user_id = message.from_user.id
            data = {'description': description_point}
            name_point_temp = self.BD.select_temp_point_user(user_id=user_id)
            self.BD.updata_point(name_point=name_point_temp, data=data)
            data = {
                'temp_point': ''
            }
            self.BD.update_user(user_id=user_id, data=data)
            self.BD.update_state_user(user_id=user_id, state=config.STATE['START_MENU'])
            # t = self.BD.select_point(name=name_point_temp)
            # self.bot.send_message(message.chat.id, MESSAGE['card_point'].format(t.name_point, t.x_coordinate, t.y_coordinate, t.h_coordinate, t.description), parse_mode="HTML")
            self.bot.send_message(message.chat.id, MESSAGE['point_add'].format(name_point_temp), parse_mode="HTML", reply_markup=self.keybords.start_menu())
