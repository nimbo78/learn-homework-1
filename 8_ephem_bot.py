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
import logging
import settings
import ephem
from datetime import date

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log'
)

def planet(bot, update):
    current_date = date.today().strftime("%d/%m/%Y")
    user_input = update.message.text.split(' ')[-1].title()
    planets = [name for _0, _1, name in ephem._libastro.builtin_planets()]
    if user_input in planets:
        planet_obj = getattr(ephem, user_input)(current_date)
        try:
            planet_constellation = ephem.constellation(planet_obj)[-1]
        except TypeError:
            update.message.reply_text(f'{user_input} is a moon..')
        update.message.reply_text(f'{user_input} in {planet_constellation} at {current_date}')
    else:
        update.message.reply_text(f'I do not know what is the {user_input} is..')

def greet_user(bot, update):
    text = 'Вызван /start'
    print(text)
    update.message.reply_text(text)


def talk_to_me(bot, update):
    user_text = update.message.text 
    print(user_text)
    update.message.reply_text(user_text)
 

def main():
    mybot = Updater(settings.API_KEY)
    
    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(CommandHandler("planet", planet))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))
    
    mybot.start_polling()
    mybot.idle()
       

if __name__ == "__main__":
    main()
