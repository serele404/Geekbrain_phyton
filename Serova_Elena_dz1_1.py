#Задание№1
#Реализовать вывод информации о промежутке времени в зависимости от его продолжительности duration в секундах: до минуты: <s> сек; до часа: <m> мин <s> сек; до суток: <h> час <m> мин <s> сек; * в остальных случаях: <d> дн <h> час <m> мин <s> сек.
duration = int(input('Введите количество секунд:'))
#вывод информации секунды:
if duration < 60:
  print('Продолжительность составляет:', duration, 'сек.')
#вывод информации минуты, секунды:
elif 60 <= duration and duration < 3600:
  minute = duration // 60
  second = duration % 60
  print('Продолжительность составляет:', minute, 'мин.', second, 'сек.')
#вывод информации часы, минуты, секунды:
elif 3600 <= duration and duration < 86400:
  hour = duration // 3600
  duration = duration % 3600
  minute = duration // 60
  second = duration % 60
  print ('Продолжительность составляет:', hour, 'ч.', minute, 'мин.', second, 'сек.')
elif 86400 <= duration and duration < 604800:
  day = duration // 86400
  duration = duration % 86400
  hour = duration // 3600
  duration = duration % 3600
  minute = duration // 60
  second = duration % 60
  print('Продолжительность составляет:', day, 'д.', hour, 'ч.', minute, 'мин.', second, 'сек.')