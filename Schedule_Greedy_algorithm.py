Schedule = {}
Schedule["Рисование"] = [9.00, 10.00]
Schedule["Английский"] = [9.30, 10.30]
Schedule["Математика"] = [10.00, 11.00]
Schedule["Информатика"] = [10.30, 11.30]
Schedule["Музыка"] = [11.00, 12.00]

result = [value for value in Schedule.values()]
del result[1:]

Schedule_temp = Schedule.copy()

for key in Schedule_temp.keys():
    if result[0] in Schedule_temp.values():
        del Schedule_temp[key]
        break

tmp = []

for i in result:
    for j in range(len(i)):
        tmp.append(i[j])

for i in Schedule_temp.values():
    for j in range(len(i)):
        if i[0] >= tmp[1]:
            tmp = i
            result.append(i)

for i in range(len(result)):
    for key, value in Schedule.items():
        if result[i] == value:
            print(key)
            break
