import time

res = 0
print('А сейчас время для квиза!')
time.sleep(1)
print('Что можно видеть с закрытыми глазами? (Введите ответ в единственном числе)')
answer = input('')
if answer in ['сон', 'Сон']:
    res += 2
print('Сколько месяцев в году имеют 28 дней? (В ответе введите число)')
answer = input('')
if answer == '12':
    res += 2
print('Какой болезнью на земле никто не болел?')
answer = input('')
if answer in ['морская', 'морской']:
    res += 2
print('Маленький, серенький на слона похож. Кто это?')
answer = input('')
if answer in ['слонёнок', 'слоненок']:
    res += 2
print("Какие часы показывают верное время только два раза в сутки?")
answer = input('')
if answer in ['сломанные', 'поломанные', 'не работающие']:
    res += 2
print('Ваш результат:', res, '/ 10')
