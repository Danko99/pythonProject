#27. TOP — 5 минимальных
z = int(input())
listz = [int(i) for i in input().split()]
temp_list = []
for i in listz:
    temp_list.sort(reverse=True)
    if len(temp_list) == 5:
        if i < min(temp_list):
            temp_list.pop(0)
            temp_list.append(i)
        print(*temp_list)
    else:
        temp_list.append(i)
        print(*temp_list)








