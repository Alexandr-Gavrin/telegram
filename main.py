from telegram.ext import Updater, MessageHandler, Filters
from telegram.ext import CallbackContext, CommandHandler

TOKEN = '620473623:AAHGmWT2-NRSivii37elUlp1uKe5WNYGauM'


def echo(update, context):
    update.message.reply_text(update.message.text)


def start(update, context):
    update.message.reply_text('Привет! Я - эхо-бот!. Напиши мне что нибудь!')


def help(update, context):
    update.message.reply_text('Я пока не умею помогать!((')


def main():
    updater = Updater(TOKEN, use_context=True)
    text_handler = MessageHandler(Filters.text, echo)
    dp = updater.dispatcher
    dp.add_handler(text_handler)
    dp.add_handler(CommandHandler('start', start))
    dp.add_handler(CommandHandler('help', help))
    updater.start_polling()
    updater.idle()


if __name__ == "__main__":
    main()
