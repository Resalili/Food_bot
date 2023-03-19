import telebot
from time import sleep
from telebot.types import BotCommand


bot = telebot.TeleBot("5853245281:AAHSoc8aWIHGJomPTKb697PnLECkT566S5E")
commands = [BotCommand('start', 'меню'),
            BotCommand('tomat', 'помидор'), 
            BotCommand('cucumber', 'огурец'),
            BotCommand('cheese', 'сыр',),
            BotCommand('sausage', 'колбаса'),
            BotCommand('melon', 'дыня'),
            BotCommand('watermelon', 'арбуз'),
            BotCommand('spam', 'спам'),]
bot.set_my_commands(commands)
@bot.message_handler(commands=['start'])
def start(message):  
    mess= "Привет, {}".format(message.from_user.first_name)
    bot.send_message(message.chat.id, mess)

@bot.message_handler(commands=['tomat'])
def tomat(message):
    img = open("tomat.png","rb")
    bot.send_photo(message.chat.id,img)

@bot.message_handler(commands=['cucumber'])
def cucumber(message):
    img = open("cucumber.png","rb")
    bot.send_photo(message.chat.id,img)

@bot.message_handler(commands=['cheese'])
def cheese(message):
    img = open("cheese.png","rb")
    bot.send_photo(message.chat.id,img)

@bot.message_handler(commands=['sausage'])
def sausage(message):
    img = open("sus.png","rb")
    bot.send_photo(message.chat.id,img)

@bot.message_handler(commands=['melon'])
def melon(message):
    img = open("melon.png","rb")
    bot.send_photo(message.chat.id,img)

@bot.message_handler(commands=['watermelon'])
def watermelon(message):
    img = open("watermelon.png","rb")
    bot.send_photo(message.chat.id,img)
@bot.message_handler(commands=['spam'])
def spam(message):
    for e in range(20):
        img = open("watermelon.png","rb")
        bot.send_photo(message.chat.id,img)
        sleep(0.5)
bot.polling(none_stop=True)
