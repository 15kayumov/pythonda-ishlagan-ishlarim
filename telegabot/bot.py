import telebot
TOKEN= '7116015745:AAH1EbXw5RSNduc2zKIZeSSVsfT9KXWkkh4'
bot = telebot.TeleBot(TOKEN, parse_mode=None) # You can set parse_mode by default. HTML or MARKDOWN
from transliterate import to_cyrillic,to_latin

@bot.message_handler(commands=['start'])
def send_welcome(message):
	bot.reply_to(message, "ASALOM ALEYKUM XUSH KELIBSIZ BIZANI BOTIMIZGA ")

@bot.message_handler(commands=['help'])
def send_welcome(message):
	bot.reply_to(message, "Sizga qanaqadir yordam kerak bo'lsa manabu userga yozvoring\n admin useri: @kayumov_15")
	
@bot.message_handler(func=lambda m: True)
def echo_all(message):
    msg=message.text
    if msg.isascii():
       javob=to_cyrillic(msg)
    else:
        javob=to_latin(msg)
    bot.reply_to(message,javob)


bot.infinity_polling()
