# импортируем класс HandlerCommands обработка комманд
from handlers.handler_com import HandlerCommands
from handlers.handler_add_user import HandlersAddUser
from handlers.handler_all_text import HandlersAllText
from handlers.handler_add_point import HandlersAddPoint
from handlers.handler_inline_query import HandlerInlineQuery
from handlers.handler_search_point import HandlersSearchPoint
# импортируем класс HandlerAllText обработка нажатия на кнопки и иные сообщения
# from handlers.handler_all_text import HandlerAllText
# импортируем класс HandlerInlineQuery обработка нажатия на кнопки инлайн
# from handlers.handler_inline_query import HandlerInlineQuery
# from handlers.handler_admin import HandlerAdmin


class HandlerMain:
    """
    Класс компоновщик
    """

    def __init__(self, bot):
        # получаем нашего бота
        self.bot = bot
        # здесь будет иницаилизация обработчиков
        self.handler_commands = HandlerCommands(self.bot)
        self.handler_add_user = HandlersAddUser(self.bot)
        self.handler_all_text = HandlersAllText(self.bot)
        self.handler_add_poin = HandlersAddPoint(self.bot)
        self.handler_inline_query = HandlerInlineQuery(self.bot)
        self.handler_search_point = HandlersSearchPoint(self.bot)

    def handle(self):
        # здесь будет запуск обработчиков
        self.handler_commands.handle()
        self.handler_add_user.handle()
        self.handler_all_text.handle()
        self.handler_add_poin.handle()
        self.handler_inline_query.handle()
        self.handler_search_point.handle()