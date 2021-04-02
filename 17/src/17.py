import collections


# 17. Казино
def Freq(b):
    arr = collections.Counter(b).most_common()
    tempArr = []
    itemMax = arr[0][1]
    for i in arr:
        if i[1] > itemMax:
            itemMax = i[1]
    for item in arr:
        if item[1] == itemMax:
            tempArr.append(item[0])
    return tempArr


red = [1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36]  # Список черных номеров
black = [2, 4, 6, 8, 10, 11, 13, 15, 17, 20, 22, 24, 26, 28, 29, 31, 33, 35]  # Список красных номеров
count_red = 0  # Количество выпавших красных
count_black = 0  # Количество выпавших черных
elem = []  # Выпавшие номера
not_most_frequent = list(range(1, 36 + 1, 1))  # Список невыпавших номеров

i = 0
while i < 36:
    n = int(input())
    if n < 0:
        break
    elem.append(n)
    print(*Freq(elem), sep=" ")  # Чаще всего за все игры
    if not_most_frequent.__contains__(n):
        not_most_frequent.remove(n)
    if red.__contains__(n):
        count_red += 1
    if black.__contains__(n):
        count_black += 1
    print(*not_most_frequent, sep=" ")  # Невыпавшие номера
    print(f'{count_red} {count_black}')  # Количество выпавших красных и черных
