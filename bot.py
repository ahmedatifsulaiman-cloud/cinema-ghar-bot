import telebot
import os

TOKEN = os.getenv("TOKEN")  # Railway will provide this
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start','help'])
def start(m):
    bot.reply_to(m, "🎬 Welcome to Cinema Ghar! Send a movie name.")

@bot.message_handler(func=lambda m: True)
def movie_search(m):
    txt = m.text.lower()
    if "kgf" in txt:
        bot.reply_to(m, "💥 KGF — example link: https://example.com/kgf")
    elif "pathaan" in txt:
        bot.reply_to(m, "🎬 Pathaan — example link: https://example.com/pathaan")
    else:
        bot.reply_to(m, "❌ Not found. Try another name.")

print("Bot started")
bot.infinity_polling()