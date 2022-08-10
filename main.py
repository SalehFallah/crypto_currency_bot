import telebot
import requests

TOKEN = '5303588108:AAEZx_NcdRcrYPdiCRmCKp5sKVXyMreuFbo'
bot = telebot.TeleBot(TOKEN)
URL = "https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT"


@bot.message_handler(commands=['start', 'help', 'hello'])
def send_welcome(message):
    bot.reply_to(message, "Welcome to crypto currencies bot!")


@bot.message_handler(func=lambda m: True)
def show_price(message):
    symbol = message.text.upper()
    response = requests.get(f"https://api.binance.com/api/v3/ticker/price?symbol={symbol}")
    print(response)
    if response.status_code == 200:
        data = response.json()
        print(data)
        bot.reply_to(message, f"{data['symbol']} price is {data['price']}")
    else:
        bot.reply_to(message, " Your Symbol is not true")


bot.infinity_polling()
