# импортируем класс родитель
from handlers.handler import Handler
# импортируем сообщения пользователю
from settings.message import MESSAGE
from settings import config
from handlers.handler_search_point import HandlersSearchPoint


class HandlerInlineQuery(Handler):
    """
    Класс обрабатывает входящие текстовые
    сообщения от нажатия на inline кнопки
    """

    def __init__(self, bot):
        super().__init__(bot)

    def press_btn_skip(self, call, chat, user_id):
        """
        Обрабатывает входящие запросы на нажатие inline кнопки "Пропустить"
        """
        state_user = self.BD.state_user(user_id)
        if state_user == config.STATE['STEP_3']:
            self.bot.send_message(chat, MESSAGE['add_step_4'], parse_mode="HTML",
                                  reply_markup=self.keybords.btn_skip())
            self.BD.update_state_user(user_id=user_id, state=config.STATE['STEP_4'])
        if state_user == config.STATE['STEP_4']:
            data = {
                'temp_point': ''
            }
            self.BD.update_user(user_id=user_id, data=data)
            name_point_temp = self.BD.select_temp_point_user(user_id=user_id)
            self.BD.update_state_user(user_id=user_id, state=config.STATE['START_MENU'])
            self.bot.send_message(chat, MESSAGE['point_add'].format(name_point_temp), parse_mode="HTML", reply_markup=self.keybords.start_menu())

    def press_btn_edit_point(self, call, chat, user_id):
        self.BD.update_state_user(user_id=user_id, state=config.STATE['EDIT_POINT'])
        self.bot.send_message(chat, 'Что желаете поправить:',
                              reply_markup=self.keybords.edit_point(),
                              parse_mode="HTML")

    def press_btn_del_point(self, call, chat, user_id):
        name_point_temp = self.BD.select_temp_point_user(user_id=user_id)
        self.BD.update_state_user(user_id=user_id, state=config.STATE['DELETE_POINT'])
        self.bot.send_message(chat, 'Подтвердите удаление точки: <b><i>{}</i></b>'.format(name_point_temp),
                              reply_markup=self.keybords.confirmation_point(),
                              parse_mode="HTML")

    def press_btn_yes_del_point(self, call, chat, user_id):

        name_point_temp = self.BD.select_temp_point_user(user_id=user_id)
        self.BD.del_point(name=name_point_temp)
        data = {
            'temp_point': ''
        }
        self.BD.update_user(user_id=user_id, data=data)

        self.bot.send_message(chat, 'Точка <b><i>{}</i></b> удалена из БД.'.format(name_point_temp),
                              parse_mode="HTML")
        self.BD.update_state_user(user_id=user_id, state=config.STATE['SEARCH'])

    def press_btn_negative(self, chat, user_id):
        self.BD.update_state_user(user_id=user_id, state=config.STATE['SEARCH'])
        self.bot.send_message(chat, MESSAGE['search'],
                              parse_mode="HTML", reply_markup=self.keybords.remove_menu())


    def edit_name_point(self, call, chat, user_id):
        self.BD.update_state_user(user_id=user_id, state=config.STATE['EDIT_NAME'])
        self.bot.send_message(chat, MESSAGE['edit_name'])

    def edit_coordinates_poit(self, call, chat, user_id):
        self.BD.update_state_user(user_id=user_id, state=config.STATE['EDIT_COORDINATE'])
        self.bot.send_message(chat, MESSAGE['edit_coordinate'])

    def edit_description_point(self, call, chat, user_id):
        self.BD.update_state_user(user_id=user_id, state=config.STATE['EDIT_DESCRIPTION'])
        self.bot.send_message(chat, MESSAGE['edit_description'])

    def edit_image_point(self, call, chat, user_id):
        self.BD.update_state_user(user_id=user_id, state=config.STATE['EDIT_IMAGE'])
        self.bot.send_message(chat, MESSAGE['edit_image'])

    def handle(self):
        # обработчик(декоратор) запросов от нажатия на кнопки товара.
        @self.bot.callback_query_handler(func=lambda call: True)
        def callback_inline_all(call):
            code = call.data
            print(code)
            user_id = call.from_user.id
            chat = call.message.chat.id
            if code == config.KEYBOARD['SKIP']:
                self.press_btn_skip(call, chat, user_id)
            if code == config.KEYBOARD['EDIT_POINT']:
                self.press_btn_edit_point(call, chat, user_id)
            if code == config.KEYBOARD['DELETE_POINT']:
                self.press_btn_del_point(call, chat, user_id)
            if code == config.KEYBOARD['YES'] and self.BD.state_user(user_id) == config.STATE['DELETE_POINT']:
                self.press_btn_yes_del_point(call, chat, user_id)
            if code == config.KEYBOARD['NEGATIVE'] and self.BD.state_user(user_id) == config.STATE['DELETE_POINT']:
                self.press_btn_negative(chat, user_id)
            if code == config.KEYBOARD['EDIT_NAME']:
                self.edit_name_point(call, chat, user_id)
            if code == config.KEYBOARD['EDIT_COORDINATE']:
                self.edit_coordinates_poit(call, chat, user_id)
            if code == config.KEYBOARD['EDIT_IMAGE']:
                self.edit_image_point(call, chat, user_id)
            if code == config.KEYBOARD['EDIT_DESCRIPTION']:
                self.edit_description_point(call, chat, user_id)
            elif self.BD.state_user(user_id) == config.STATE['SEARCH']:
                data = {
                    'temp_point': code,
                }
                self.BD.update_user(user_id=user_id, data=data)
                HandlersSearchPoint(self.bot).search_point(point=code, message=call.message)

