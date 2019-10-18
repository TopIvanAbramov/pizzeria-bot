from services.DataBase import DB

phrases = {
    "menu": {
        "ru": "Меню",
        "eng": "Menu"
    },

    "select_menu": {
        "ru": "Что вас интересует?",
        "eng": "Select an option"
    },

    "make_order": {
        "ru": "Сделать заказ",
        "eng": "Make order"
    },

    "leave_feedback": {
        "ru": "Оставить отзыв о боте",
        "eng": "Leave feedback about bot"
    },

    "cancel": {
        "ru": "Отменить",
        "eng": "Cancel"
    },

    "write_feedback": {
        "ru": "Напишите отзыв о боте",
        "eng": "Send feedback about this bot"
    },

    "thank_you_feedback": {
        "ru": "Спасибо за отзыв! Мы ценим ваше мнение",
        "eng": "Thanks for the feedback! We appreciate your feedback"
    },

    "send_name": {
        "ru": "Отправить название",
        "eng": "Send the product name"
    },

    "call_staff": {
        "ru": "‍Позвать сотрудника магазина",
        "eng": "Call a store employee"
    },

    "greeting": {
        "ru": 'Привет! Я чат бот кафе  "Cacio e vino" в г. Иннополис',
        "eng": 'Hello! I am the chat bot of "Cacio e vino" cafe in the Innopolis city'
    },

    "call_waiter": {
        "ru": "‍Позвать официанта",
        "eng": "Call a waiter"
    },

    "staff_request_sent": {
        "ru": "Запрос отправлен",
        "eng": "Request has been sent"
    },

    "call_admin": {
        "ru": "️Позвать администратора",
        "eng": "Call store administrator"
    },

    "who_to_call": {
        "ru": "Кого вы хотите позвать?",
        "eng": "Who do you want to call"
    },
}

def translate(key: str, language: str):
    return phrases[key][language]


def extract_language_and_update_if_not_present(update, context):
    if "language" not in context.user_data:
        language_preference = DB('language_selection', chat_id="TEXT", language="TEXT")
        language = language_preference.get_items(chat_id=update.message.chat_id)
        if len(language) == 0:
            language_preference.add_item(chat_id=update.message.chat_id, language="ru")
            context.user_data["language"] = "ru"
        else:
            context.user_data["language"] = language[0][1]

    return context.user_data["language"]