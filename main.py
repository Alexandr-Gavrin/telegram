from telegram.ext import Updater, MessageHandler, Filters


def echo(update, context):
    update.message.reply_text(f'Я получил сообщение {update.message.text}.')


def main():
    updater = Updater('1187007411:AAE61PeWLmJRb9BD9U2L9dIV-igj0fq3Uxs', use_context=True)
    dp = updater.dispatcher
    text_handler = MessageHandler(Filters.text, echo)
    dp.add_handler(text_handler)
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
