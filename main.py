from flask import Flask
from threading import Thread
import os
import telebot

app = Flask('')

@app.route('/')
def home():
    return "RS Tour Bot Alive"

def run():
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))

def keep_alive():
    Thread(target=run).start()

keep_alive()

TOKEN = os.environ.get('TOKEN')
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "Bot অন আছে ভাই ✅")

bot.polling()
