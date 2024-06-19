import telebot
from telebot import types
from main import xmlToList
import re
from const import token

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

@bot.message_handler(commands=['group'])
def start(message):
    start = bot.reply_to(message, 'Напишите Группу')
    bot.register_next_step_handler(start, alert)

def alert(message):
    print(remove_special_characters(message.text))

bot.polling()