"""
Домашнее задание №1

Использование библиотек: ephem

* Установите модуль ephem
* Добавьте в бота команду /planet, которая будет принимать на вход 
  название планеты на английском, например /planet Mars
* В функции-обработчике команды из update.message.text получите 
  название планеты (подсказка: используйте .split())
* При помощи условного оператора if и ephem.constellation научите 
  бота отвечать, в каком созвездии сегодня находится планета.

"""
import ephem
import logging
import settings

from datetime import datetime
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

logging.basicConfig(format='%(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot2.log'
                    )

#def main():
    #mybot = Updater("API_KEY", request_kwargs=PROXY)
    #...
    
def main():
    mybot = Updater(settings.API_KEY, request_kwargs=settings.PROXY)
    
    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(CommandHandler('planet', talk_to_me))
    dp.add_handler(CommandHandler('not_solar', not_solar))
    dp.add_handler(MessageHandler(Filters.text, planet_user))

    
    mybot.start_polling()
    mybot.idle()

def greet_user(bot, update):
    text = 'Вызван /start, введите /planet'
    #print(text)
    update.message.reply_text(text)

def not_solar(bot, update):
    text = 'Это не планета Солнечной системы, введите /planet'
    print(text)
    update.message.reply_text(text)

def talk_to_me(bot, update):
    text = 'Введите название планеты на английском: '
    print(text)
    update.message.reply_text(text)

def planet_user(bot, update):
    planets = ['Mars', 'Venus', 'Sun', 'Mercury', 'Earth', 'Jupiter', 'Saturn', 'Uranus', 'Neptune', 'Pluto']
    dt_now = datetime.now()
    planet_name = str(update.message.text.lower().capitalize())
    if planet_name in planets:
        planet = getattr(ephem, planet_name) (dt_now)
        #planet.compute()
        planet_user = ephem.constellation(planet)
        print(planet_user)
        update.message.reply_text(planet_user)
    else:
        print(not_solar)

if __name__ == "__main__":
    main()
