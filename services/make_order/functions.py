from telegram import ReplyKeyboardMarkup, KeyboardButton
from telegram.ext import ConversationHandler
from services.initial.configure import menu
from services.languages import extract_language_and_update_if_not_present, translate
from services.Stats import *

ADD_COMMENT = 0


def make_order(update, context):
    bot = context.bot

    lang = extract_language_and_update_if_not_present(update, context)

    bot.send_message(update.message.chat_id, "Заглушка")

    menu(update, context)

    edit_stat("make_order")

    edit_user_stat(update.message.chat_id, "make_order")

    edit_daily_active_users_stat(update.message.chat_id)

    return ConversationHandler.END