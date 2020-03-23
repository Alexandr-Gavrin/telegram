from telegram.ext import Updater, MessageHandler, Filters
from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove
from telegram.ext import CallbackContext, CommandHandler

TOKEN = '620473623:AAHGmWT2-NRSivii37elUlp1uKe5WNYGauM'
reply_keyboard = [['/address', '/phone'], ['/site', '/work_time']]
markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=False)


def echo(update, context):
    update.message.reply_text(update.message.text)


def start(update, context):
    update.message.reply_text('Привет! Я - эхо-бот!. Напиши мне что нибудь!', reply_markup=markup)


def help(update, context):
    update.message.reply_text('Я пока не умею помогать!((')


def address(update, context):
    update.message.reply_text('Адрес: г. Гусь-Хрустальный, Микрорайон, д. 53')


def phone(update, context):
    update.message.reply_text('Телефон: +4123111')


def site(update, context):
    update.message.reply_text('Сайт: hh.ru')


def work_time(update, context):
    update.message.reply_text('11-22')


def close_keyboard(update, context):
    update.message.reply_text('OK', reply_markup=ReplyKeyboardRemove)


def main():
    updater = Updater(TOKEN, use_context=True)
    text_handler = MessageHandler(Filters.text, echo)
    dp = updater.dispatcher
    dp.add_handler(text_handler)
    dp.add_handler(CommandHandler('start', start))
    dp.add_handler(CommandHandler('help', help))
    dp.add_handler(CommandHandler('address', address))
    dp.add_handler(CommandHandler('phone', phone))
    dp.add_handler(CommandHandler('site', site))
    dp.add_handler(CommandHandler('work_time', work_time))
    dp.add_handler(CommandHandler('close', close_keyboard))
    updater.start_polling()
    updater.idle()


if __name__ == "__main__":
    main()
