from services.initial.functions import *
from telegram.ext import MessageHandler, Filters, CommandHandler
from services.languages import phrases
from services.make_order.functions import *
from services.common_items import cancel


def setup(updater):
    dispatcher = updater.dispatcher

    adding_comment = ConversationHandler(
        entry_points=[
            MessageHandler(Filters.regex('|'.join(phrases["make_order"].values())), make_order)],
        states={
            ADD_COMMENT: [MessageHandler(Filters.regex("^🚫(Отменить|Cancel)$"), cancel)],
        },
        fallbacks=[MessageHandler(Filters.all, cancel)]
    )

    dispatcher.add_handler(adding_comment)