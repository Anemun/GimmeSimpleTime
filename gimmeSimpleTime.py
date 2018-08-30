import telebot
from sys import argv
from telebot import types
from datetime import datetime

TELEGRAM_BOT_TOKEN = argv[1]
bot = telebot.TeleBot(TELEGRAM_BOT_TOKEN)

version = "0.3"
timeFormat = '%Y-%m-%d %H:%M:%S'

@bot.message_handler(commands=["time"])
def getTime(message):
    bot.send_message(text=str(datetime.now().strftime(timeFormat)), chat_id=message.chat.id)

@bot.message_handler(commands=["ver"])
def getVersion(message):
    bot.send_message(text=version, chat_id=message.chat.id)

# это постоянное прослушивание сообщений, чтобы запускать обработчики выше. Должно быть В САМОМ КОНЦЕ ФАЙЛА
if __name__ == '__main__':
    bot.polling(none_stop=True)
    