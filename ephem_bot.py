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
    dp.add_handler(CommandHandler("planet", greet_user))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))
    
    mybot.start_polling()
    mybot.idle()

def greet_user(bot, update):
    text = 'Введите /planet'
    #print(text)
    update.message.reply_text(text)

planets = ['Mars', 'Venus', 'Sun', 'Mercury', 'Earth', 'Jupiter', 'Saturn', 'Uranus', 'Neptune', 'Pluto']
dt_now = datetime.now()
def talk_to_me(bot, update):
    user_text = update.message.planets.split()
    if user_text in planets:
        user_planet = ephem.user_text(dt_now)
        item = ephem.constellation(user_planet)
        print(item)
    update.message.reply_text(user_text)
          

if __name__ == "__main__":
    main()
