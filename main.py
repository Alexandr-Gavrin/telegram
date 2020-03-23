from telegram.ext import Updater, MessageHandler, Filters
from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove
from telegram.ext import CallbackContext, CommandHandler, ConversationHandler

TOKEN = '620473623:AAHGmWT2-NRSivii37elUlp1uKe5WNYGauM'
reply_keyboard = [['/address', '/phone'], ['/site', '/work_time']]
markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=False)



def start(update, context):
    update.message.reply_text('Привет. Пройдите небольшой опрос\n'
                              'Вы можете прервать опрос, /stop\n'
                              'В каком городе вы живёте?')
    return 1


def first_response(update, context):
    city = update.message.text
    update.message.reply_text(f'Какая погода в {city}?')
    return 2


def second_response(update, context):
    weather = update.message.text
    print(weather)
    update.message.reply_text('Спасибо за участие в опросе!')
    return ConversationHandler.END


def stop(update, context):
    update.message.reply_text('Диалог окончен. Выберите следующее действие!')


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


def task(context):
    job = context.job
    context.bot.send_message(job.context, text='Вернулся!')


def set_timer(update, context):
    chat_id = update.message.chat_id
    try:
        due = (context.args[0])
        if due < 0:
            update.message.reply_text('Извините, мы не умеем возварщатсья в прошлое')
            return
        if 'job' in context.chat_data:
            old_job = context.chat_data['job']
            old_job.shedule_removal()
        new_job = context.job_queue.run_once(task, due, context=chat_id)
        context.chat_data['job'] = new_job
        update.message.reply_text(f'Вернусь через {due} секунд')
    except (IndexError, ValueError):
        update.message.reply_text('Использование: /set <секунд>')


def echo(update, context):
    # У объекта класса Updater есть поле message,
    # являющееся объектом сообщения.
    # У message есть поле text, содержащее текст полученного сообщения,
    # а также метод reply_text(str),
    # отсылающий ответ пользователю, от которого получено сообщение.
    update.message.reply_text('ВОРОНКОВА ХАХАХ')


def unset_timer(update, context):
    if 'job' not in context.chat_data:
        update.message.reply_text('Нет таймера!')
        return
    job = context.chat_data['job']
    job.shedule_removal()
    del context.chat_data['job']
    update.message.reply_text('Вернулся')


def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher
    text_handler = MessageHandler(Filters.text, echo)
    dp.add_handler(text_handler)
    updater.start_polling()
    updater.idle()


if __name__ == "__main__":
    main()
