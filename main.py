import xml.etree.ElementTree as ET

from itertools import groupby
from operator import itemgetter

from function import *
from const import *

def xmlToList( group, date):

    group = convert_to_group(group)
    date = convert_to_date(date)

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

    result.sort(key=itemgetter('date'))

    grouped_data = {k: list(v) for k, v in groupby(result, key=itemgetter('date'))}
    sorted_data = sorted(grouped_data.get(date), key=lambda x: int(x['lesson']))

    array = []
    for item in sorted_data:
        array.append('''
<b>Урок №:</b> <i>{lesson}</i>
<b>Предмет:</b> {subject}
<b>Кабинет:</b> {cabinet}
<b>Корпус:</b> {departament}
<b>Учитель:</b> {teacher}
'''.format(lesson = item['lesson'], subject = item['subject'], cabinet = item['cabinet'], departament = item['departament'], teacher = item['teacher']))

    res = ''
    for i in range(len(array)):
        res += array[i]

    return res


