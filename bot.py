from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging
import settings

logging.basicConfig(format='%(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log'
                    )

def main():
    mybot = Updater("API_KEY", request_kwargs=PROXY)
    ...

def main():
    mybot = Updater(settings.API_KEY, request_kwargs=settings.PROXY)

    dp = mybot.dispatcher#диспетчер принимает входящие и раскидывает по получателям
    dp.add_handler(CommandHandler("start", greet_user))#CommandHandler - обработчик команд
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))#MessageHandler - обработчик сообщений, Filters показывает, с каким типом сообщений мы хотим работать


    mybot.start_polling()#mybot, начни регул.ходить на платформу телеграм и проверяй наличие сообщений
    mybot.idle()# mybot будет работать, пока мы его принудительно не остановим

def greet_user(bot, update):
    print('Вызван /start')
    print(text)
    update.message.reply_text(text)

def talk_to_me(bot, update):
    user_text = update.message.text 
    print(user_text)
    update.message.reply_text(user_text)

main()# вызов функции
