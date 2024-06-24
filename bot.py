import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

from main import xmlToList
from const import token
from function import *

bot = telebot.TeleBot(token)
# Хранилище для счетчиков
counters = {}

@bot.message_handler(commands=['start'])
def welcome(message):
	bot.send_message(message.chat.id, '<i>Привет!</i> 👋\n\n<b>Я помогу тебе узнать расписание на нужную дату 📝</b>\n\nДля дальнейшей работы напиши /get', parse_mode='HTML')

@bot.message_handler(commands=['get'])
def get(message):
	chat_id = message.chat.id
	counters[chat_id] = [] 
	message_bot = bot.send_message(message.chat.id,"👥 Введи <b>Группу</b> с разделительным знаком\n\nНапример: <code>ИС 1.20</code>", parse_mode='HTML')
	bot.register_next_step_handler(message_bot, date)

def date(message):
	chat_id = message.chat.id
	counters[chat_id].append(convert_to_group(message.text))
	message_bot = bot.send_message(message.chat.id,"📅 Введи <b>Дату</b> с разделительными(пробелы, точки, слэши) знаками. Указать нужно в формате: <code>ДД.ММ.ГГ</code>\n\nНапример: <code>17.06.24</code>", parse_mode='HTML')
	bot.register_next_step_handler(message_bot, alert)

def create_markup(chat_id):
	markup = InlineKeyboardMarkup()
	decrement_button = InlineKeyboardButton('<', callback_data=f'decrement_{chat_id}')
	increment_button = InlineKeyboardButton('>', callback_data=f'increment_{chat_id}')
	markup.add(decrement_button, increment_button)

	return markup

def alert(message):
	chat_id = message.chat.id
	counters[chat_id].append(convert_to_date(message.text))
	markup = create_markup(chat_id)
	listing = xmlToList(counters[chat_id][0], counters[chat_id][1])
	
	bot.send_message(message.chat.id, listing, parse_mode = 'HTML', reply_markup = markup)

@bot.callback_query_handler(func=lambda call: True)
def handle_callback_query(call):
	chat_id = call.message.chat.id
	markup = create_markup(chat_id)
	
	try:
		if f'increment_{chat_id}' in call.data:
			counters[chat_id][1] = increment_date(counters[chat_id][1])
		elif f'decrement_{chat_id}' in call.data:
			counters[chat_id][1] = deincrement_date(counters[chat_id][1])

		listing = xmlToList(counters[chat_id][0], counters[chat_id][1])
		bot.edit_message_text(listing, chat_id=chat_id, message_id=call.message.message_id,parse_mode = 'HTML', reply_markup=markup)

	except:
		bot.send_message(call.message.chat.id, '⚠ Ошибка: <code>Неправильная дата</code> \n\nНапишите повторно /get', parse_mode = 'HTML')



bot.polling()
