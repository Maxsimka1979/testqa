import telebot


bot = telebot.TeleBot('6498543552:AAEL7JpUqAo2AnAytglm_CSVe73GdH5TJoc')
@bot.message_handler(content_types=['voice', ])
def repeat(message: telebot.types.Message):
    bot.send_message(message.chat.id, 'у тебя красивый голос')

bot.polling(none_stop=True)

