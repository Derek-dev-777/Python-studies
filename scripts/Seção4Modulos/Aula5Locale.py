import calendar
import locale

locale.setlocale(locale.LC_ALL, "") # esse codigo faz com que o python traduza tudo para o idioma do meu sitema

print(calendar.calendar(2025))