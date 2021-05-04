bool_val = True

class Alchohol:
    name = ''
    price = 0
    v = 0
    final_price = price
    final_v = v
    numb_of_bottle = 0
    last_money = 0

    def check_price(self):
        global l_money
        global bool_val
        if self.price > l_money or l_money < 0:
            bool_val = False
            self.final_v = 0

        else:
            z = self.price
            while z <= l_money:
                self.final_price += self.price
                self.final_v += self.v
                self.numb_of_bottle += 1
                z += self.price
            self.last_money = l_money - self.final_price


money = int(input())
l_money = money
k = int(input())
arr_v = []
for i in range(k):
    arr_v.append(0)
bool_arr = []
for i in range(k):
    bool_arr.append(False)
alco = []
for i in range(k):
    alco.append(Alchohol())

boolean_for_cicle = True
max_ = 0
max_ind = 0
i = 0

while bool_val:
    while i < k:

        if boolean_for_cicle:
            alco[i].name, alco[i].price, alco[i].v = input().split()
            alco[i].price = int(alco[i].price)
            alco[i].v = int(alco[i].v)

        if not bool_arr[i]:
            alco[i].check_price()
            arr_v.insert(i, alco[i].final_v)
            max_ = max(arr_v)
            max_ind = arr_v.index(max(arr_v))

        if i == k - 1:
            bool_arr[max_ind] = True
            l_money = alco[max_ind].last_money
            boolean_for_cicle = False
            if max_ == 0:
                bool_val = False
                break

        i += 1
    max_ = 0
    max_ind = 0
    arr_v.clear()
    for i_ in range(k):
        arr_v.append(0)

    j = 0
    while j < len(bool_arr):
        if bool_arr[j] == False:
            alco[j].final_v = 0
            alco[j].final_price = 0
            alco[j].numb_of_bottle = 0
        j += 1

    if bool_arr.count(True) == k:
        bool_val = False

    i = 0

output_v = 0
x = 0
while x < len(bool_arr):
    if bool_arr[x] == True and alco[x].numb_of_bottle != 0:
        print(alco[x].name, alco[x].numb_of_bottle)
        output_v = output_v + alco[x].final_v
    x += 1

print(output_v)
print(l_money)

if bool_arr.count(False) == k:
    print("-1")
    exit()
