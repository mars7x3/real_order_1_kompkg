
import telebot
import time

from orm_mysql import chek_price
from decouple import config



bot = telebot.TeleBot(config('TOKEN'))

@bot.message_handler(commands=['Erjigit777',])
def start_message(message):
    counter = 0
    while True:
        counter += 1
        
        chat_id = message.chat.id
        try:
            bot.send_message(chat_id, f'----- START {counter} -----')
            
            bot.send_message(chat_id, f"----- FINISH {counter} -----\nПотраченое ремя --- {chek_price()}")
        except Exception as e:
            bot.send_message(chat_id, f'----- ERROR -----\nОшибка при выполнении задачи! {e}')
        time.sleep(3600)


bot.polling()


