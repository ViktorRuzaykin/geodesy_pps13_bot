welcome_new_user = """
🌐<b>Приветствую!</b>, данный бот 
создан для информационного обмена между геодезистами и производителями работ на ППС-13. Чтобы воспользоваться этим, 
для начало нужно зарегистрироваться в системе. Пришлите Ваше <b>ФИО</b> через пробел, \n например, <b><i>Иванов Иван Иванович</i></b>
"""


get_user_phone = """
📞Теперь отправьте Ваш <b>номер
телефона</b> через <b>+7</b> следующим сообщением:
"""

get_specialization = """
👷Отлично! Теперь укажите Вашу должность: 
"""

error_user_name = """
📛⛔<b>ФИО</b> должны быть 
введены через один <i>пробел</i>, и должны 
быть написаны через <i>кириллицу</i>. Также 
должны быт <i>заглавные буквы</i>. Например, <b><i>Иванов Иван Иванович</i></b>. Учтите
формат и попробуйте снова:
"""

error_user_phone = """
⛔📛⛔<b>Номер телефона</b> должен 
содержать 11 цифр и должен обязательно 
содержать в начале <b>+7. Учтите
формат и попробуйте снова</b>: 
"""

welcome_to_bot = """
🏗<b>Добро пожаловать</b> <i>в главное меню 
чaт-бота ГЕОДЕЗИЯ ППС-13.</i>Просто воспользуйтесь <b><i>меню</i></b>, что бы взаимодействовать с функциями бота:
"""

set_orientation = """
🏗Выберите <b>Направление строительства</b>: 
"""

set_code_project = """
☎Укажите <b>Шифр</b> проекта:
"""

set_object = """
🛸Укажите <b>Объект/Номер</b> позиции:
"""

set_project_section = """
🧩Укажите <b>Раздел проекта</b>:
"""

set_number_sheet = """
№📄Укажите <b>Номер листа проекта</b>:
"""

set_type_work = """
⛏Укажите <b>Конструктив</b>: 
"""

set_location = """
🗼Укажите <b>Пикатаж/Номер трубы ТК/Номер колодца</b>:
"""

set_status_doc = """
🗽Укажите <b>Статус ИС</b>:
"""

set_scheme = """
🗺Отправьте <b>Схему</b>:
"""

set_comment = """
📋Введите <b>Примечание</b>:
"""


MESSAGE = {
    'welcome_new_user': welcome_new_user,
    'get_user_phone': get_user_phone,
    'error_user_name': error_user_name,
    'error_user_phone': error_user_phone,
    'welcome_to_bot': welcome_to_bot,
    'get_specialization': get_specialization,
    'set_orientation': set_orientation,
    'set_code_project': set_code_project,
    'set_object': set_object,
    'set_project_section': set_project_section,
    'set_number_sheet': set_number_sheet,
    'set_type_work': set_type_work,
    'set_location': set_location,
    'set_status_doc': set_status_doc,
    'set_scheme': set_scheme,
    'set_comment': set_comment,
}
