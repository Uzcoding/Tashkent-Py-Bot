from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging
import config


logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log')

def start(update, context):
    text = 'Hello I\'m Tashkent Py'
    context.bot.send_message(chat_id=update.effective_chat.id, text=text)

def talk_to_me(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text= 'Привет {}! Ты написал: {}'.format(update.message.chat.first_name, update.message.text))
    logging.info('User: %s, Chat id: %s, Message: %s',
                 update.message.chat.username,
                 update.message.chat.id,
                 update.message.text )

def main():
    mybot = Updater(token=config.TOKEN, use_context=True)

    dp = mybot.dispatcher
    dp.add_handler( CommandHandler('start', start) )
    dp.add_handler(MessageHandler( Filters.text, talk_to_me) )

    mybot.start_polling()
    mybot.idle()

main()