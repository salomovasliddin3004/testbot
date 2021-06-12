from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext


def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(f'Hello {update.effective_user.first_name}')


updater = Updater('1766280930:AAHtKtuWbjSx_vpQmO1UNR4g_QkBqR6zd6I')

updater.dispatcher.add_handler(CommandHandler('start', start))

updater.start_polling()
updater.idle()