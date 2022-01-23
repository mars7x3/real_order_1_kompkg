
import telebot

from orm_mysql import chek_price
from decouple import config



bot = telebot.TeleBot(config('TOKEN'))

@bot.message_handler(commands=['Erjigit777',])
def start_message(message):
    chat_id = message.chat.id
    bot.send_message(chat_id, f'Привет {message.chat.first_name}!')
    try:
        bot.send_message(chat_id, '----- START -----')
        
        bot.send_message(chat_id, f"----- FINISH -----\nРабота заняла {chek_price()}")
    except Exception as e:
        bot.send_message(chat_id, f'----- ERROR -----\nОшибка при выполнении задачи! {e}')


bot.polling()


