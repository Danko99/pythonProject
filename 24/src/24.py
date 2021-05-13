#24. Работа с json
import json

with open('in.json') as f:
    templates = json.load(f)

count = {}

for todo in templates:
    if todo["completed"]:
        try:
            # Увеличение количества существующих пользователей.
            count[todo["userId"]] += 1
        except KeyError:
            # Новый пользователь, ставим кол-во 1.
            count[todo["userId"]] = 1


list = []

for key in count:
    dict_out = {}
    dict_out["task_completed"] = count[key]
    dict_out["userId"] = key
    list.append(dict_out)

with open("out.json", "w") as write_file:
    json.dump(list, write_file)


