import re 

list = ['1$ 120',
 '1С 12 0',
 '1с 12.0',
 'и$ 120',
 'иС 120',
 'т.к 12.0',
 'мр 1.20',
 'ИС120',
 'Ис 120']






for item in list:
	print(remove_special_characters(item))
