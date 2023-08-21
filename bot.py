import telebot


bot = telebot.TeleBot('6498543552:AAEL7JpUqAo2AnAytglm_CSVe73GdH5TJoc')

@bot.message_handler(commands=['start', 'help'])
def repeat(message: telebot.types.Message):
    bot.reply_to(message, f'Приветсвую, {message.chat.active_username}')

bot.polling(none_stop=True)