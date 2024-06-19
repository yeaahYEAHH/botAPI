import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

from main import xmlToList
from const import token
from function import *

bot = telebot.TeleBot(token)

# def renderBtnDay( ):
#     keyBoard = types.InlineKeyboardMarkup(row_width = 2)
#     btnPrevDay = types.InlineKeyboardButton(text='Предыдущий день', callback_data='prevDay')
#     btnNextDay = types.InlineKeyboardButton(text = 'Следующий день', callback_data = 'nextDay')
#     keyBoard.add(btnPrevDay, btnNextDay)

#     return keyBoard

# @bot.message_handler(commands=['start'])
# def start(message):
#     bot.send_message(message.chat.id, '<b>Дата</b> [текущая дата] | <b>Группа</b> [текущая группа]', parse_mode = 'HTML', reply_markup = renderBtnDay())

# @bot.callback_query_handler(func = lambda callback : callback.data)
# def checkCallBack(callback):
#     if callback.data == 'prevDay':
#         bot.edit_message_text(chat_id=callback.message.chat.id, message_id = callback.message.id, text = '<b>Дата</b> [предыдущая дата] | <b>Группа</b> [текущая группа]', parse_mode = 'HTML', reply_markup = renderBtnDay())

#     if callback.data == 'nextDay':
#         bot.edit_message_text(chat_id=callback.message.chat.id, message_id = callback.message.id, text = '<b>Дата</b> [следующая дата] | <b>Группа</b> [текущая группа]', parse_mode = 'HTML', reply_markup = renderBtnDay())

# array = []

# @bot.message_handler(commands=['get'])
# def group(message):
# 	message_bot = bot.send_message(message.chat.id,'Группа')
# 	bot.register_next_step_handler(message_bot, date)


# def date(message):
# 	array.append(message.text)
# 	start = bot.send_message(message.chat.id,'Дату')
# 	bot.register_next_step_handler(start, alert)

# def alert(message):
# 	array.append(message.text)
# 	[group, date] = array
# 	listing = xmlToList(group, date)
# 	bot.send_message(message.chat.id, listing, parse_mode = 'HTML', reply_markup = renderBtnDay())

# @bot.callback_query_handler(func = lambda callback : callback.data)
# def checkCallBack(callback):
# 	[group, date] = array
# 	if callback.data == 'prevDay':
# 		bot.edit_message_text(chat_id=callback.message.chat.id, message_id = callback.message.id, text = xmlToList(group,deincrement_date(date)), parse_mode = 'HTML', reply_markup = renderBtnDay())

# 	if callback.data == 'nextDay':
# 		bot.edit_message_text(chat_id=callback.message.chat.id, message_id = callback.message.id, text = xmlToList(group,increment_date(date)), parse_mode = 'HTML', reply_markup = renderBtnDay())

# bot.polling()


# Хранилище для счетчиков
counters = {}

@bot.message_handler(commands=['start'])
def send_welcome(message):
	chat_id = message.chat.id
	counters[chat_id] = '19.05.24'  # Инициализируем счетчик для каждого пользователя

	markup = create_counter_markup(chat_id)
	bot.send_message(chat_id, f'Счетчик: {counters[chat_id]}', reply_markup=markup)

def create_counter_markup(chat_id):
	markup = InlineKeyboardMarkup()
	increment_button = InlineKeyboardButton('Следующий день', callback_data=f'increment_{chat_id}')
	decrement_button = InlineKeyboardButton('Предыдущий', callback_data=f'decrement_{chat_id}')
	markup.add(increment_button, decrement_button)
	return markup

@bot.callback_query_handler(func=lambda call: True)
def handle_callback_query(call):
	chat_id = call.message.chat.id
	if f'increment_{chat_id}' in call.data:
		counters[chat_id] = increment_date(counters[chat_id])
	elif f'decrement_{chat_id}' in call.data:
		counters[chat_id] = deincrement_date(counters[chat_id])

	markup = create_counter_markup(chat_id)
	print(counters)
	bot.edit_message_text(f'Счетчик: {counters[chat_id]}', chat_id=chat_id, message_id=call.message.message_id, reply_markup=markup)

if __name__ == '__main__':
    bot.polling(none_stop=True)
