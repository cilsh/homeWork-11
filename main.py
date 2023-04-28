import telebot


bot = telebot.TeleBot('')


@bot.message_handler(commands=['start'])
def start(ctx):
    bot.send_message(ctx.chat.id, 'Привіт!')


@bot.message_handler(content_types=['text'])
def text(ctx):
    bot.send_message(ctx.chat.id, eval(ctx.text))


bot.polling()
