# 9. Встреча
from datetime import datetime

time = input()
time2 = input()

datetime_object = datetime.strptime(f'{time}', '%I:%M')
datetime_object2 = datetime.strptime(f'{time2}', '%I:%M')

if datetime_object2 < datetime_object:
    print('Неверное время')
    exit()

result = (datetime_object2 - datetime_object).seconds/60
print(result)
if result > 15:
    print('Встреча не состоится')
else:
    print('Встреча состоится')

