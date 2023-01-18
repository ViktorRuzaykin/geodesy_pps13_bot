from handlers.handler import Handler
from settings import config
from settings.message import MESSAGE


class HandlersSearchPoint(Handler):
    """
    Класс обрабатывает сообщения от пользователя при добавлении новой точки
    """

    def __init__(self, bot):
        super().__init__(bot)

    def search_point(self, point, message):
        print('call search_point')
        user_id = message.from_user.id
        data = {
            'temp_point': point,
        }
        self.BD.update_user(user_id=user_id, data=data)
        name_all_points = self.BD.select_all_point()

        if point in name_all_points:
            point_card = self.BD.select_point(name=point)
            if point_card.image_path:
                photo = open(point_card.image_path, 'rb')
                self.bot.send_photo(message.chat.id,
                                    photo=photo,
                                    caption=MESSAGE['card_point'].format(
                                        point_card.name_point,
                                        point_card.x_coordinate,
                                        point_card.y_coordinate,
                                        point_card.h_coordinate,
                                        point_card.description),
                                    parse_mode="HTML",
                                    reply_markup=self.keybords.set_step())
            else:
                self.bot.send_message(message.chat.id, MESSAGE['card_point'].format(
                    point_card.name_point,
                    point_card.x_coordinate,
                    point_card.y_coordinate,
                    point_card.h_coordinate,
                    point_card.description), parse_mode="HTML",
                                      reply_markup=self.keybords.set_step()
                                      )

        else:

            self.bot.send_message(message.chat.id, MESSAGE['search_error'], parse_mode="HTML")
            s_point = []
            for i in name_all_points:
                if point in i:
                    s_point.append(i)
            print(len(s_point))
            if s_point:
                self.bot.send_message(message.chat.id, '📋Но есть что-то похожее:',
                                      parse_mode="HTML",
                                      reply_markup=self.keybords.set_select_all_point(sorted(s_point)))

    def handle(self):
        # обработчик(декоратор) сообщений
        @self.bot.message_handler(
            func=lambda message: (self.BD.state_user(message.from_user.id)) == config.STATE['SEARCH'])
        def search(message):
            s_point = message.text.lower()
            self.search_point(point=s_point, message=message)
