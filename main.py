import telebot
import messages_manager

bot = telebot.TeleBot('1106970175:AAEy9zcQuLWhWMPEw6C1ME0RGWm2X_c_ijg')

messages_manager.init(bot)

bot.polling()