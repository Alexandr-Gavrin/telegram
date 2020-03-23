from telegram.ext import Updater, MessageHandler, Filters
from telegram.ext import CallbackContext, CommandHandler


TOKEN = '620473623:AAHGmWT2-NRSivii37elUlp1uKe5WNYGauM'



def echo(update, context):
    update.message.reply_text(update.message.text)


def main():
    updater = Updater(TOKEN, use_context=True)
    text_handler = MessageHandler(Filters.text, echo)
    dp = updater.dispatcher
    dp.add_handler(text_handler)
    updater.start_polling()
    updater.idle()


if __name__ == "__main__":
    main()
