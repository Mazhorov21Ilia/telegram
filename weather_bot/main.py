from telebot import TeleBot
from pars import get_forecast
from datetime import datetime

token = "yor-token"
bot = TeleBot(token=token)


@bot.message_handler(commands=['start'])
def send_welcome(message):
	bot.reply_to(message, "Напишите дату в ближайшие 14 дней в формате гггг-мм-дд")

def search_weather(date =datetime.today()):
	weather = get_forecast(date).get("forecast").get("forecastday")[0]
	avg_temp = weather.get("day").get("avgtemp_c")
	data = weather.get("date")
	avg_weather = weather.get("day").get("condition").get("text")
	photo = weather.get("day").get("condition").get("icon").split("/")
	photo[-3] = '128x128'
	return [f"Погода: {avg_weather}\nТемпература: {avg_temp}°C, дата: {data}", ("/").join(photo[2:])]

@bot.message_handler()
def zaglushka(message):
	date = message.text
	text = search_weather(date)
	bot.send_photo(
		chat_id=message.chat.id, 
		photo=text[1],
		reply_to_message_id=message.id,
		caption=text[0]
				)
	

if __name__ == "__main__":
	bot.infinity_polling()
