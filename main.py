import re
import xml.etree.ElementTree as ET
from const import *
import pprint


def xmlToList( group, date):
    root = ET.fromstring(response(group, date))

    namespaces = {
        'ns0': 'http://schemas.xmlsoap.org/soap/envelope/',
        'ns1': 'http://www.neftpk.ru/Schedule',
        'xsi': 'http://www.w3.org/2001/XMLSchema-instance',
    }

    result = []
    for tab in root.findall('.//ns1:Tab', namespaces=namespaces):
        entry = {
            'teacher': tab.find('ns1:UF_ID_TEACHER', namespaces=namespaces).text,
            'group': tab.find('ns1:UF_ID_GROUP', namespaces=namespaces).text,
            'subject': tab.find('ns1:UF_ID_SUBJECT', namespaces=namespaces).text,
            'lesson': tab.find('ns1:UF_PARA', namespaces=namespaces).text,
            'cabinet': tab.find('ns1:UF_LECTURE', namespaces=namespaces).text,
            'departament': tab.find('ns1:UF_ZONE', namespaces=namespaces).text,
            'date': tab.find('ns1:UF_DATE', namespaces=namespaces).text.replace(' 0:00:00', '')
        }
    
        result.append(entry)

    array = []
    for item in result:
        array.append('''
Урок № {lesson}
Дата: {date}
Предмет: {subject}
Кабинет: {cabinet}
Корпус: {departament}
Учитель: {teacher}'''.format(lesson = item['lesson'], date = item['date'], subject = item['subject'], cabinet = item['cabinet'], departament = item['departament'], teacher = item['teacher']))




    
    return array


test = xmlToList( 'ИС 1.23', '22.11.2023')
