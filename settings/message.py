welcome_new_user = """
☀<b>Доброго времени суток</b>, бот 
создан, чтобы собирать ГЕО точки(марки) в одном месте и быстро находить их. Чтобы воспользоваться этим, 
пришлите для начала Ваше <b>Имя</b> и <b>Фамилию</b>
"""

get_user_phone = """
📞Теперь отправьте Ваш <b>номер
телефона</b> через <b>+7</b> следующим сообщением:
"""

error_user_name = """
📛⛔<b>Имя</b> и <b>Фамилия</b> должны быть 
введены через один <i>пробел</i>, и должны 
быть написаны через <i>кириллицу</i>. Также 
должны быт <i>заглавные буквы</i>. <b>Учтите
формат и попробуйте снова</b>:
"""

error_user_phone = """
⛔📛⛔<b>Номер телефона</b> должен 
содержать 11 цифр и должен обязательно 
содержать в начале <b>+7. Учтите
формат и попробуйте снова</b>: 
"""

welcome_to_bot = """
✈<b>Добро пожаловать</b> <i>в главное меню 
чaт-бота GeoPointsBot. </i>Здесь Вы можете добавлять точки(марки) в базу данных и быстро находить в нужное время. 
Просто воспользуйтесь <b><i>меню</i></b>, что бы взаимодействовать с функциями бота:
"""

add_step_1 = """
<b><i>Шаг 1/4.</i></b>📝Напишите имя точки:
"""

add_step_2 = """
<b><i>Шаг 2/4.</i></b>🌐Напишите координаты точки X Y Z через пробел:
"""

add_step_3 = """
<b><i>Шаг 3/4.</i></b>🖼Прикрепите одну фотографию точки или пропустите этот пункт:
"""

add_step_4 = """
<b><i>Шаг 4/4.</i></b>📝Добавьте описание точки или пропустите этот пункт:
"""

error_step_1 = """
⛔📛Такая точка уже существует в базе данных.
"""
error_step_2 = """
⛔📛В данном пункте нужно обязательно написать координаты X Y Z через пробел. Должно быть три значения.
Например <i>125.32 3254.32 28.32</i> 
"""

point_add = """
Точка <b><i>{}</i></b> успешно добавлена в базу данных.
"""

card_point = """
<b><i>\nИмя точки:</i></b> {}
<b><i>\nX:</i></b> {}
<b><i>\nY:</i></b> {}
<b><i>\nH:</i></b> {}
<b><i>\nОписание:</i></b> {}      
"""

search = """
<b><i>🔍Отправьте имя точки для поиска.</i></b>
"""
search_error = """
⛔📛Такой точки в базе данных нет.
"""

download_point = """
Загрузить точки. Отправь <b>ОДИН</b> файл с каталогом координат. Файл должен быть с расширением .txt \n
Разделение колонок через запятую!\nname,x,y,h   
"""

error_all_point = """
🤪Их слишком много🤪\n<b><i>{}шт</i></b>.
"""

edit_name = """
📝Напишите новое имя точки:
"""

edit_coordinate = """
🌐Напишите новые координаты точки X Y Z через пробел:
"""

edit_image = """
🖼Прикрепите новую фотографию точки.
"""

edit_description = """
📝Добавьте новое описание точки:
"""


MESSAGE = {
    'welcome_new_user': welcome_new_user,
    'get_user_phone': get_user_phone,
    'error_user_name': error_user_name,
    'error_user_phone': error_user_phone,
    'welcome_to_bot': welcome_to_bot,
    'add_step_1': add_step_1,
    'add_step_2': add_step_2,
    'add_step_3': add_step_3,
    'add_step_4': add_step_4,
    'error_step_1': error_step_1,
    'error_step_2': error_step_2,
    'card_point': card_point,
    'point_add': point_add,
    'search': search,
    'search_error': search_error,
    'download_point': download_point,
    'error_all_point': error_all_point,
    'edit_name': edit_name,
    'edit_coordinate': edit_coordinate,
    'edit_image': edit_image,
    'edit_description': edit_description,
}