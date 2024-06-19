import re 
def formatingDate(inputDate):
    pattern = re.search(r'\d+', inputDate)
    cleanedString = pattern.sub('', inputString)





def formatingGroup(inputString):
	pattern = re.compile(r'[^a-zA-Zа-яА-Я0-9]')

	cleanedString = pattern.sub('', inputString)
	while cleanedString and not cleanedString[0].isalpha():
		cleanedString = cleanedString[1:]
	
	return cleanedString.upper()

list = ['zIZ;|bUnSXm3',
 ']}oa:z5!+YxE',
 'wjbD(4qu]_m$',
 'z^<8PjB80\\tS',
 '"G;l-a_%ps,4',
 'mY{!W-JmL*Z3',
 "fgUbn71DE['[",
 ',(z?c31{/b[V',
 '{`b,4PM:AU-9',
 '6OkjIVea8tw=']

from datetime import datetime

now = datetime.now()

for item in list:

    pattern = re.search(r'\d+', item)
    cleanedString = pattern[0]
    lengthString = len(cleanedString)
    if lengthString in [1, 2]:
        cleanedString = if int(cleanedString)
        formatted_date_time = now.strftime(".%m.%Y")
        print('0' + str(cleanedString))

    # if lengthString in [3, 4]:

    # if lengthString in [6, 8]:





# # Форматирование даты и времени

# print("Форматированная дата и время:", formatted_date_time)

# # Форматирование только даты
# formatted_date = now.strftime("%Y-%m-%d")
# print("Форматированная дата:", formatted_date)

# # Форматирование только времени
# formatted_time = now.strftime("%H:%M:%S")
# print("Форматированное время:", formatted_time)
