# 15. Угадай число
from random import randrange


def game():
    random = randrange(100)

    print('{Приветственное сообщение от игры}')
    s = 0
    while s <= 5:
        if s == 5:
            print(f'Вы проиграли. Было загадано: {random}')
            break
        s += 1
        n = int(input())
        if n < random:
            print('Загаданное число больше')
            continue
        elif n > random:
            print('Загаданное число меньше')
            continue
        elif n == random:
            print('Поздравляю! Вы угадали')
            break



game()
while True:
    flag = input('Хотите начать сначала? (1 - ДА )')

    if flag == '1':
        game()
    else:
        break
