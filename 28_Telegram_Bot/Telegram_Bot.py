from typing import Final

from nbformat.v1 import new_text_cell
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

#Constants
TOKEN: Final[str] = '7422842865:AAESE5iK2ajetBo8FIdfeWgypNAHiGG84R0'
BOT_USER_NAME: Final[str] = '@cool_spirit7_bot'


async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Hello There! Nice to meet you. Let\'s chat.')

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Type something and I will respond.')

async def custom_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('This is just a custom command.')


def handle_response(text: str) -> str:
    processed: str = text.lower()

    if 'hello' in processed:
        return 'Hello There!'

    if 'how are you' in processed:
        return 'I am Good, Thanks!'

    if 'I love python' in processed:
        return 'Python is cooooooool'

    return 'Sorry! I do not understand.'


async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message_type: str = update.message.chat.type
    text: str = update.message.text

    print(f'User ({update.message.chat.id}) in {message_type}: "{text}"')

    if message_type == 'group':
        if BOT_USER_NAME in text:
            new_text: str = text.replace(BOT_USER_NAME, '').strip()
            response: str = handle_response(new_text)

        else:
            return
    else:
        response: str = handle_response(text)

    print('Bot: ', response)
    await update.message.reply_text(response)

async def error(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(f'Update: {update} caused erro: {context.error}')


def main() -> None:
    print('Starting the bot...')

    app = Application.builder().token(TOKEN).build()

    #Commands
    app.add_handler(CommandHandler('start', start_command))
    app.add_handler(CommandHandler('help', help_command))
    app.add_handler(CommandHandler('custom', custom_command))

    #Messages
    app.add_handler(MessageHandler(filters.TEXT, handle_message))

    #Error
    app.add_error_handler(error)

    print("Polling...")
    app.run_polling(poll_interval=5)


if __name__ == '__main__':
    main()


