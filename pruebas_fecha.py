import locale
from datetime import datetime

locale.setlocale(locale.LC_ALL, 'de_DE')
date_str_es = '27-Octubre-2020'  # es_ES locale
datetime_object = datetime.strptime(date_str_es, '%d-%B-%Y')
print(datetime_object)