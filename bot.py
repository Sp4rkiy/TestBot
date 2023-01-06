import  telebot
bot = telebot.TeleBot("5879327773:AAE0Ps9q2bmEJX_ISpmKkNBpn5jFrjJ6nYU")

@bot.message_handler(commands=["start"])
def ajuste(message):
     bot.reply_to(message, "alo")

if __name__=="__main__":
     print("Ejecutando")
     bot.infinity_polling()
     print("fin")
