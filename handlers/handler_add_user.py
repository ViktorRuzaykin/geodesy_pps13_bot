from handlers.handler import Handler
from settings import config
from settings.message import MESSAGE
import re

class HandlersAddUser(Handler):
    """
    Класс обрабатывает сообщения от пользователя при регистрации
    """

    def __init__(self, bot):
        super().__init__(bot)

    def handle(self):

        @self.bot.message_handler(
            func=lambda message: (self.BD.state_user(message.from_user.id)) == config.STATE['NAME'])
        def user_entering_name(message):
            user_id = message.from_user.id
            user_message = message.text.split(' ')
            print(user_message)
            if len(user_message) == 2 and user_message[0][0].isupper() and user_message[1][0].isupper():
                # self.bot.send_message(message.chat.id, user_phone)
                self.bot.send_message(message.chat.id, MESSAGE['get_user_phone'], parse_mode="HTML")
                data_user = {
                    'first_name': user_message[0],
                    'last_name': user_message[1],
                }
                self.BD.update_user(user_id=user_id, data=data_user)
                self.BD.update_state_user(user_id, config.STATE['PHONE'])
            else:
                self.bot.send_message(message.chat.id, MESSAGE['error_user_name'], parse_mode="HTML")

        @self.bot.message_handler(
            func=lambda message: (self.BD.state_user(message.from_user.id)) == config.STATE['PHONE'])
        def user_entering_phone(message):
            user_id = message.from_user.id
            user_phone = message.text
            match = re.fullmatch(r'[+]7\d{10}', user_phone)
            if match:
                data_user = {
                    'phone': user_phone,
                }
                self.BD.update_user(user_id=user_id, data=data_user)

                self.bot.send_message(message.chat.id, MESSAGE['welcome_to_bot'],
                                      parse_mode="HTML", reply_markup=self.keybords.start_menu())
                self.BD.update_state_user(user_id, config.STATE['START_MENU'])
            else:
                self.bot.send_message(message.chat.id, MESSAGE['error_user_phone'],
                                      parse_mode="HTML", )
