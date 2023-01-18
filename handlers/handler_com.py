# импортируем класс родитель
from handlers.handler import Handler
from handlers.handler_add_user import HandlersAddUser
from settings import config
from settings.message import MESSAGE


class HandlerCommands(Handler):
    """
    Класс обрабатывает входящие команды /start и /help и т.п.
    """

    def __init__(self, bot):
        super().__init__(bot)
        # self.admin_com = HandlerAdmin(self.bot)
        # self.user_com = HandlerAllText(self.bot)

    def _start_user_registration(self, message):
        id_user = message.from_user.id
        users = self.BD.select_user(id_user)
        if not users:
            # print('Такого нет!')
            user_name = message.from_user.username
            self.BD.add_user(id_user, user_name)

        self.keybords.remove_menu()
        self.bot.send_message(message.chat.id, MESSAGE['welcome_new_user'],
                              parse_mode="HTML")


    def pressed_btn_start(self, message):
        """
        Обрабатывает входящие /start команды
        """
        id_user = message.from_user.id
        user = self.BD.select_user(id_user)
        # проверяем есть ли пользователь в БД
        if user:
            if user[0].state == 'NAME' or user[0].state == 'PHONE':
                self.BD.update_state_user(id_user, config.STATE['NAME'])
                self._start_user_registration(message)
            else:
                self.BD.update_state_user(id_user, config.STATE['START_MENU'])
                self.bot.send_message(message.chat.id, MESSAGE['welcome_to_bot'],
                                      parse_mode="HTML", reply_markup=self.keybords.start_menu())
        else:
            # если нет регистрируем нового пользователя
            self._start_user_registration(message)



    def handle(self):
        # обработчик(декоратор) сообщений,
        # который обрабатывает входящие /start, /admin команды.
        @self.bot.message_handler(commands=['start'])
        def handle(message):
            if message.text == '/start':
                self.pressed_btn_start(message)
