from telegram.ext import Updater
from services.initial.configure import setup as setup_initial
from services.feedback.configure import setup as setup_feedback
from services.call_staff.configure import setup as setup_call_staff
from services.make_order.configure import setup as setup_make_order

import os

import logging
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')


def main():
    TOKEN = os.environ['BOT_TOKEN']
    updater = Updater(TOKEN, use_context=True)
    setup_feedback(updater)
    setup_call_staff(updater)
    setup_make_order(updater)
    setup_initial(updater)
    updater.start_polling(poll_interval=1)


if __name__ == '__main__':
    main()