import re 
from datetime import datetime
from datetime import timedelta

# Функция для преобразования даты в формат ДД.ММ.ГГГГ
def convert_to_date(date_str):
    # Определяем шаблоны для различных форматов дат
    date_patterns = [
        (r'(\d{1,2})[ /.](\d{1,2})[ /.](\d{2,4})', '%d.%m.%Y')  # шаблон для различных разделителей
    ]
    
    for pattern, date_format in date_patterns:
        match = re.match(pattern, date_str)
        if match:
            day, month, year = match.groups()
            
            # Приводим год к формату ГГГГ
            if len(year) == 2:
                year = '20' + year
            
            # Создаем объект даты
            date_obj = datetime.strptime(f"{day}.{month}.{year}", '%d.%m.%Y')
            # Возвращаем строку в формате ДД.ММ.ГГГГ
            return date_obj.strftime('%d.%m.%Y')
    
    # Если формат даты не распознан, возвращаем исходную строку (или можно бросить исключение)
    return date_str


# Функция для преобразования группы в формату ИС 1.20
def convert_to_group(input_string):
    # Регулярное выражение для удаления всех спецсимволов, кроме букв и цифр
    pattern = re.compile(r'[^a-zA-Zа-яА-Я0-9]')
    # Замена всех найденных символов на пустую строку
    cleaned_string = pattern.sub('', input_string)
    # Проверка и удаление первых символов, если они не буквы
    while cleaned_string and not cleaned_string[0].isalpha():
        cleaned_string = cleaned_string[1:]

    return (cleaned_string[:2] + ' ' + cleaned_string[2] + '.' + cleaned_string[-2:]).upper()

#Увелечение дня
def increment_date(date):
    date_obj = datetime.strptime(date, "%d.%m.%Y")
    date_obj = date_obj + timedelta(days=1)
    date_str = date_obj.strftime("%d.%m.%Y")

    return date_str

#Уменьшение дня 
def deincrement_date(date):
    date_obj = datetime.strptime(date, "%d.%m.%Y")
    date_obj = date_obj - timedelta(days=1)
    date_str = date_obj.strftime("%d.%m.%Y")

    return date_str
