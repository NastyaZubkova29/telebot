import telebot
bot=telebot.TeleBot('6513633249:AAFugEPkgRDrFVPPOqYbPU9JF8FvfKfuQ4c')

@bot.message_handler(commands=['start'])
def main(msg):
    markup = telebot.types.InlineKeyboardMarkup(row_width=1)
    but1 = telebot.types.InlineKeyboardButton('Москва', callback_data='first')
    but2 = telebot.types.InlineKeyboardButton('Виловатово', callback_data='second')
    markup.add(but1, but2)
    bot.send_message(msg.chat.id, 'Выбери кнопку ниже:', reply_markup=markup)
@bot.callback_query_handler(func=lambda call:True)
def callback(call):
    if call.message:
        if call.data=='first':
            bot.send_message(call.message.chat.id, 'Это столица нашей страны')
        if call.data=='second':
            bot.send_message(call.message.chat.id, 'Это твоё родное село')


bot.infinity_polling()
