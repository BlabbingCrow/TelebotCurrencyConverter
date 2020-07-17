import decimal

from currency_converter import get_currency_cost

def init(bot):
    @bot.message_handler(commands=['start'])
    def start_message(message):
        bot.send_message(message.chat.id, 'Привет, начнем работу с конвертацией валют')

    @bot.message_handler(commands=['help'])
    def start_message(message):
        bot.send_message(message.chat.id, 'Список возможных команд:\n/convert [код валюты из которой перевести] [код валюты в которую перевести] [сумма]\nПример:/convert USD RUB 100')


    @bot.message_handler(commands=["convert"])
    def answer(message):
        msg_text = message.text[len("/convert "):]
        args = msg_text.split()
        costFirst = 1
        costSecond = 1

        if len(args) != 3:
            bot.send_message(message.chat.id, "Некорректные аргументы")
            return

        if args[0] != "RUB":
            costFirst = get_currency_cost(args[0])
        if args[1] != "RUB":
            costSecond = get_currency_cost(args[1])
        if costFirst != None and costSecond != None:
            try:
                num = decimal.Decimal(args[2])
            except:
                bot.send_message(message.chat.id, "Некорректные аргументы")
                return

            cost = costFirst / costSecond * num
            bot.send_message(message.chat.id, cost)
        else:
            bot.send_message(message.chat.id, "Валюты с таким именем не найдено")

    @bot.message_handler(content_types=['text'])
    def send_text(message):
        if message.text == 'Привет':
            bot.send_message(message.chat.id, 'Привет, конвертируем валюту?')
        elif message.text == 'Пока':
            bot.send_message(message.chat.id, 'Пока, бизнесмен')
        else:
            bot.send_message(message.chat.id, 'Я вас не понимаю, воспользуйтесь командой /help, если вы не знаете о чем меня попросить')