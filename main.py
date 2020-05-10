from telegram.ext import Updater, MessageHandler, Filters
from telegram.ext import CommandHandler
import time


def date(update, context):
    t = time.localtime()
    data = time.asctime(t).split()
    update.message.reply_text(f'Date - {data[0]} {data[1]} {data[2]} {data[4]}')


def times(update, context):
    t = time.localtime()
    data = time.asctime(t).split()
    update.message.reply_text(f'Time - {data[3]}')


def main():
    updater = Updater('1187007411:AAE61PeWLmJRb9BD9U2L9dIV-igj0fq3Uxs', use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("time", times))
    dp.add_handler(CommandHandler("date", date))
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
