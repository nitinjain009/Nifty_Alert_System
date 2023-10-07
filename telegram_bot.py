import telebot
from dotenv import load_dotenv
import os

load_dotenv()
GROUP_ID = os.getenv('GROUP_ID')
bot = telebot.TeleBot(os.getenv('API_KEY'))

rise_path = os.path.join(os.path.dirname(__file__), 'rise.png')
fall_path = os.path.join(os.path.dirname(__file__), 'fall.png')

def nifty_alert(message, direction):

    if direction == "rise":
        bot.send_photo(chat_id=GROUP_ID, photo=open(rise_path, 'rb'))
    elif direction == "fall":
        bot.send_photo(chat_id=GROUP_ID, photo=open(fall_path, 'rb'))
    z_button = telebot.types.InlineKeyboardButton(text='Zerodha', url='https://play.google.com/store/apps/details?id=com.zerodha.kite3&hl=en&gl=US')
    t_button = telebot.types.InlineKeyboardButton(text='Trading View', url='https://www.tradingview.com/chart/a8Jdv71A/?symbol=NSE%3ANIFTY')

    keyboard = telebot.types.InlineKeyboardMarkup()
    keyboard.add(z_button)
    keyboard.add(t_button)
    bot.send_message(chat_id=GROUP_ID, text=message, reply_markup=keyboard)
    